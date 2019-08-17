from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(object):

    def res_format(self, *args, **kwargs):
        d = dict(self.__dict__)
        d.pop('_sa_instance_state', None)

        for k in list(d):
            if k in kwargs:
                if type(kwargs[k]) == type(True) and not kwargs[k]:
                    d.pop(k, None)
                else:
                    d[k] = kwargs[k]

        return d