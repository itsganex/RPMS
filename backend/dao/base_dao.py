from backend.database import Database
class BaseDAO:
    table=""
    primary_key=""
    allowed_columns=set()
    def list(self, where="", params=(), limit=100, offset=0):
        sql=f"SELECT * FROM {self.table} " + (f"WHERE {where} " if where else "")
        sql += "ORDER BY " + self.primary_key + " DESC LIMIT %s OFFSET %s"
        return Database.fetch_all(sql, tuple(params)+(limit,offset))
    def get(self, record_id):
        return Database.fetch_one(f"SELECT * FROM {self.table} WHERE {self.primary_key}=%s",(record_id,))
    def create(self, data):
        clean={k:v for k,v in data.items() if k in self.allowed_columns}
        if not clean: raise ValueError("No valid fields supplied.")
        cols=", ".join(clean)
        marks=", ".join(["%s"]*len(clean))
        return Database.execute(f"INSERT INTO {self.table} ({cols}) VALUES ({marks})",tuple(clean.values()))[0]
    def update(self, record_id, data):
        clean={k:v for k,v in data.items() if k in self.allowed_columns}
        if not clean: raise ValueError("No valid fields supplied.")
        sets=", ".join(f"{k}=%s" for k in clean)
        return Database.execute(f"UPDATE {self.table} SET {sets} WHERE {self.primary_key}=%s",tuple(clean.values())+(record_id,))[1]
