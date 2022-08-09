from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "id": result[0],
            "make": result[1],
            "model": result[2],
            "owner_first": result[3],
            "owner_last": result[4]
        }
        out.append(vehicle)
    return out


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active = 1",()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?",
        (pk, )
    )
    results = cursor.fetchall()
    cursor
    return output_formatter(results)

def insert(vehic_dict):
    value_tuple = (
        vehic_dict.get("make"),
        vehic_dict.get("model"),
        vehic_dict.get("owner_first"),
        vehic_dict.get("owner_last"),
    )
    statement ="""
            INSERT INTO vehicle(
                make,
                model,
                owner_first,
                owner_last
            ) VALUES (?,?,?,?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit
    cursor.close()

def update(pk, vehic_data):
    value_tuple = (
        vehic_data.get("make"),
        vehic_data.get("model"),
        vehic_data.get("owner_first"),
        vehic_data.get("owner_last"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET make=?,
        model=?,
        owner_first=?,
        owner_last=?
        WHERE id=?"
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE vehicle SET active=0 WHERE id=?", (pk, ))
    cursor.commit()
    cursor.close()
