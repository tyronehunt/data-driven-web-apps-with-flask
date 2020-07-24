import os
from pypi_org.data import db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def main():
    """ Determines sequence of script for basic_inserts.py module. First initiate a db with init_db
      (defined below) and then while that is open run the inserts_a_package function """
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    """ Creates an instance (i.e. a row) for the Package class and gets user to insert column data.
    Creates an instance of the Release class and gets users to insert column data.
    As there is a relationship between Package and Release class, appends the release data to the list of
    Releases, stored in the Package class.
    """
    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input("Package summary: ").strip()
    p.author_name = input("Author: ").strip()
    p.license = input("License: ").strip()

    print("Release 1:")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))
    # Add the release to the packages list of releases
    p.releases.append(r)

    print("Release 2:")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size in bytes: "))
    p.releases.append(r)

    # In order to save the data to the sql database, you need to create a new session, then add and commit data to it
    session = db_session.create_session()
    session.add(p)
    session.commit()


def init_db():
    """ Gets absolute directory path of database file and passes it to global_init function in db_session.py"""
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    """ Tells main() function to start running here"""
    main()