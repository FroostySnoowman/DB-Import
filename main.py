import aiomysql
import asyncio
import yaml

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

filepath = data["Filepath"]
host = data["Host"]
database = data["Database"]
username = data["Username"]
password = data["Password"]
port = data["Port"]

async def import_sql_file():
    try:
        async with aiomysql.connect(host=host, port=port, user=username, password=password, db=database) as conn:
            cur = await conn.cursor()
            with open(filepath, 'r') as f:
                sql = f.read()
                await cur.execute(sql)
            await conn.commit()
            print("Import complete.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print("Import started...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(import_sql_file())