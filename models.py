from driver import DbDriver


class FacultyModel(DbDriver):
    def __init__(self):
        super().__init__()

    def get_all_faculties(self) -> list:
        query = 'SELECT * FROM Faculties'
        params = tuple()
        faculties = self.execute_select(query, params)
        return faculties

    def add_faculty(self, faculty_name: str) -> None:
        query = 'INSERT INTO Faculties (name) Values (?)'
        params = (faculty_name,)
        self.execute_dml(query, params)


class GroupModel(DbDriver):
    def __init__(self):
        super().__init__()

    def get_all_groups(self):
        return self.execute_select("""
            SELECT Groups.name, Faculties.name
            FROM Groups INNER JOIN Faculties
            On Groups.faculty_id = Faculties.id
            """, tuple())

    def add_group(self, group_name: str, faculty_name: str):
        if (faculty_name, ) in self.execute_select('SELECT name FROM Faculties', tuple()):
            faculty_id = self.execute_select('SELECT id FROM Faculties WHERE name = (?)', (faculty_name, ))[0][0]
            self.execute_dml('INSERT INTO Groups (name, faculty_id) VALUES (?, ?)', (group_name, faculty_id))
            print("Група добавлена!")
        else:
            print('Нету такого факультета!')

    def dell_group(self, group_name: str):
        if (group_name, ) in self.execute_select("SELECT name FROM Groups", tuple()):
            self.execute_dml('DELETE FROM Groups WHERE name = (?)', (group_name, ))
            print("Група удалена!")
        else:
            print("Нету такой групы!")
