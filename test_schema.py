from app.core.schema import QueryIntent

q = QueryIntent(target_table="files")
print(q.model_dump())
