import sqlite3

with sqlite3.connect('kitapxana.db') as connection:
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS kitaplar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        at TEXT NOT NULL,
        avtor TEXT NOT NULL,
        jil INTEGER,
        bet_sani INTEGER
    );
    """
    cursor.execute(create_table_query)
    print('Keste jaratildi')

    insert_query = "INSERT INTO kitaplar (at, avtor, jil, bet_sani) VALUES (?, ?, ?, ?);"
    kitaplar = [
        ("Otken kunler", "Abdulla Qodiriy", 1925, 520),
        ("Joldasi menen sirlasiw", "I.Yusupov", 1988, 150),
        ("Qaraqalpaq qizi", "T.Qayipbergenov", 1941, 350),
        ("Alpamis", "Xaliq awizeki doretpesi", 1941, 350)
    ]
    cursor.executemany(insert_query, kitaplar)
    connection.commit()

    print(f"{cursor.rowcount} kitap qosıldı.")

    select_query = "SELECT * FROM kitaplar;"
    cursor.execute(select_query)

    kitaplar_result = cursor.fetchall()
    print("\nKitaplar tızimi:")
    for kitap in kitaplar_result:
        print(kitap)

    select_by_avtor_query = "SELECT at, jil FROM kitaplar WHERE avtor = ?;"
    cursor.execute(select_by_avtor_query, ("T.Qayipbergenov",))
    kitaps = cursor.fetchall()

    print("\\nAvtori T.Qayipbergenov bolǵan kitaplar")
    for kitap in kitaps:
        print(kitap)

    select_query = "SELECT * FROM kitaplar WHERE jil > 1950;"
    cursor.execute(select_query)

    kitaplar_result = cursor.fetchall()
    print("\n1950-jıldan keyin basılǵan kitaplar:")
    for kitap in kitaplar_result:
        print(f"ID: {kitap[0]}, Atı: {kitap[1]}, Avtorı: {kitap[2]}, Jılı: {kitap[3]}, Bet sani: {kitap[4]}")

    print("\n400 betten kóp kitaplar:")
    select_query = "SELECT at, bet_sani FROM kitaplar WHERE bet_sani > 400;"
    cursor.execute(select_query)

    result = cursor.fetchall()
    for kitap in result:
        print(f"Atı: {kitap[0]}, Bet sanı: {kitap[1]}")

    jana_jil = 1989
    kitap_id = 2

    update_query = "UPDATE kitaplar SET jil = ? WHERE id = ?;"
    cursor.execute(update_query, (jana_jil, kitap_id))
    connection.commit()

    select_query = "SELECT * FROM kitaplar;"
    cursor.execute(select_query)

    kitaplar_result = cursor.fetchall()
    print("\nKitaplar tızimi:")
    for kitap in kitaplar_result:
        print(kitap)

    kitap_id = 4

    delete_query = "DELETE FROM kitaplar WHERE id = ?;"
    cursor.execute(delete_query, (kitap_id,))

    connection.commit()

    print(f"id={kitap_id} kitap oshti.")

    cursor.execute("SELECT * FROM kitaplar WHERE id = ?", (kitap_id,))
    deleted_student = cursor.fetchone()

    kitaplar_result = cursor.fetchall()
    print("\nKitaplar tızimi:")
    for kitap in kitaplar_result:
        print(kitap)


def kitap_izlew(avtor_ati):
    with sqlite3.connect('kitapxana.db') as connection:
        cursor = connection.cursor()
        avtor_ati_query = "SELECT at, jil FROM kitaplar WHERE avtor = ?;"
        cursor.execute(avtor_ati_query, (avtor_ati,))
        result = cursor.fetchall()
        if result:
            print(f"\nAvtori '{avtor_ati}' bolǵan kitaplar:")
            for kitap in result:
                print(f"Atı: {kitap[0]}, Jılı: {kitap[1]}")
        else:
            print(f"\nAvtor '{avtor_ati}' boyınsha kitap tabılmadi.")

kitap_izlew('T.Qayipbergenov')
