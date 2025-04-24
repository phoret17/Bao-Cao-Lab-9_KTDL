import os
import psycopg2
import csv

def execute_schema(cur):
    try:
        print("🔨 Đang tạo bảng...")
        script_path = os.path.join("/app", "schema.sql")
        with open(script_path, "r") as f:
            cur.execute(f.read())
        print("✅ Bảng đã được tạo thành công.")
    except Exception as e:
        print(f"❌ Lỗi khi tạo bảng: {e}")
        raise

def insert_account_data(cur, path):
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            print(f"📄 Columns in account CSV: {reader.fieldnames}")

            for row in reader:
                cur.execute("""
                    INSERT INTO accounts (customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    int(row['customer_id']), row['first_name'], row['last_name'], row['address_1'],
                    row['address_2'], row['city'], row['state'], row['zip_code'], row['join_date']
                ))
    except Exception as e:
        print(f"❌ Lỗi khi chèn dữ liệu account: {e}")
        raise

def insert_product_data(cur, path):
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            print(f"📄 Columns in product CSV: {reader.fieldnames}")

            for row in reader:
                cur.execute("""
                    INSERT INTO products (product_id, product_code, product_description)
                    VALUES (%s, %s, %s)
                """, (
                    int(row['product_id']), row['product_code'], row['product_description']
                ))
    except Exception as e:
        print(f"❌ Lỗi khi chèn dữ liệu product: {e}")
        raise

def insert_transaction_data(cur, path):
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            print(f"📄 Columns in transaction CSV: {reader.fieldnames}")

            for row in reader:
                cur.execute("""
                    INSERT INTO transactions (
                        transaction_id, transaction_date, product_id,
                        product_code, product_description, quantity, account_id
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['transaction_id'], row['transaction_date'], int(row['product_id']),
                    row['product_code'], row['product_description'], int(row['quantity']), int(row['account_id'])
                ))
    except Exception as e:
        print(f"❌ Lỗi khi chèn dữ liệu transaction: {e}")
        raise

def main():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        cur = conn.cursor()

        execute_schema(cur)

        print("⬇️ Đang insert dữ liệu...")
        insert_account_data(cur, os.path.join("data", "accounts.csv"))
        insert_product_data(cur, os.path.join("data", "products.csv"))
        insert_transaction_data(cur, os.path.join("data", "transactions.csv"))

        conn.commit()
        print("✅ Dữ liệu đã được chèn thành công.")
    except Exception as e:
        print(f"❌ Lỗi toàn cục: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    main()
