class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getatter__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('%s'%key)

    def __setattr__(self,key,value):
        self[key]=value
