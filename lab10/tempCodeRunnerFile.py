
c = conn()
cur = c.cursor()
create_table(cur)
cur.close()
c.commit()
