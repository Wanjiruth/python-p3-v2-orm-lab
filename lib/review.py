from __init__ import CURSOR, CONN
from department import Department
from employee import Employee


class Review:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, year, summary, employee_id, id=None):
        self.id = None
        self.year = year
        self.summary = summary
        self.employee_id = employee_id

    def __repr__(self):
        return (
            f"<Review {self.id}: {self.year}, {self.summary}, "
            + f"Employee: {self.employee_id}>"
        )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            year INT,
            summary TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employee(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review  instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the year, summary, and employee id values of the current Review object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        pass

    @classmethod
    def create(cls, year, summary, employee_id):
        """ Initialize a new Review instance and save the object to the database. Return the new instance. """
        pass
   
    @classmethod
    def instance_from_db(cls, row):
        """Return an Review instance having the attribute values from the table row."""
        # Check the dictionary for  existing instance using the row's primary key
        pass
   

    @classmethod
    def find_by_id(cls, id):
        """Return a Review instance having the attribute values from the table row."""
        pass

    def update(self):
        """Update the table row corresponding to the current Review instance."""
        pass

    def delete(self):
        """Delete the table row corresponding to the current Review instance,
        delete the dictionary entry, and reassign id attribute"""
        pass

    
    @classmethod
    def create(cls, year, summary, employee_id):
        review = cls(year=year, summary=summary, employee_id=employee_id)
        review.save()
        return review
    def save(self):
        if self.id is None:
            CURSOR.execute(
                'INSERT INTO reviews (year, summary, employee_id) VALUES (?, ?, ?)',
                (self.year, self.summary, self.employee_id)
            )
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                'UPDATE reviews SET year = ?, summary = ?, employee_id = ? WHERE id = ?',
                (self.year, self.summary, self.employee_id, self.id)
            )
        CONN.commit()
    @classmethod
    def instance_from_db(cls, row):
        if row:
            review = cls(year=row[1], summary=row[2], employee_id=row[3])
            review.id = row[0]
            return review
        else:
            return None
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM reviews WHERE id = ?', (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None
    @classmethod
    def get_all(cls):
        reviews = []
        CURSOR.execute('SELECT * FROM reviews')
        rows = CURSOR.fetchall()
        for row in rows:
            reviews.append(cls.instance_from_db(row))
        return reviews if reviews else []    
    