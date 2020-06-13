from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, \
    check_password_hash


class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理菜谱权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


cms_role_user = db.Table(
    # 定义角色与管理员用户多对多的中间表
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)  # 角色名称
    desc = db.Column(db.String(200), nullable=True)  # 角色描述
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)  # 权限

    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')


class CMSUser(db.Model):
    # 定义完模型之后需要通过manage.py映射到数据库
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        # 将本方法定义为一个属性【外界访问:user=CMSUser,print(user.password)】
        return self._password

    @password.setter
    def password(self, raw_password):
        """
        :param raw_password: 先对原生密码进行加密然后存储
        """
        # 设置密码的方法【是user.password = abc|而不是user.password('abc')】
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """
        :param raw_password: 检测原生密码和加密密码是否一致
        """
        result = check_password_hash(self.password, raw_password)
        return result

    @property
    def permissions(self):
        # 拿到管理员用户拥有的所有权限
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    def has_permission(self, permission):
        # 判断有没有某权限
        # all_permissions = self.permissions
        # result = all_permissions&permission == permission
        # return result
        return self.permissions & permission == permission

    @property
    def is_developer(self):
        # 判断是否使开发者【cms_base.html的CMS组管理用到if】
        return self.has_permission(CMSPersmission.ALL_PERMISSION)

# 密码对外的字段名为【password】
# 密码对内的字段名是【_password】
