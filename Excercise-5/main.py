import psycopg2
import os
from psycopg2 import sql

def main():
    conn = None  # Khởi tạo biến conn
    cursor = None  # Khởi tạo biến cursor
    try:
        # Kết nối Postgres
        conn = psycopg2.connect(
            host="localhost",
            database="airflow",
            user="airflow",
            password="airflow"
        )
        conn.autocommit = False
        cursor = conn.cursor()

        # Thực thi script tạo bảng
        with open('create_tables.sql', 'r') as sql_file:
            cursor.execute(sql_file.read())
        
        # Import dữ liệu từ CSV
        tables = ['accounts', 'products', 'transactions']
        for table in tables:
            csv_path = os.path.join('data', f'{table}.csv')
            with open(csv_path, 'r') as f:
                cursor.copy_expert(
                    sql.SQL("COPY {} FROM STDIN WITH CSV HEADER DELIMITER ','").format(
                        sql.Identifier(table)
                    ), 
                    f
                )
        
        conn.commit()
        print("Dữ liệu đã được import thành công!")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Lỗi: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()