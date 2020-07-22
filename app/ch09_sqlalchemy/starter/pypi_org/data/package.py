import datetime

import sqlalchemy as sa

from pypi_org.data.modelbase import SqlAlchemyBase


class Package(SqlAlchemyBase):
    # name your database created from class
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    # maintainers
    # releases

    license = sa.Column(sa.String, index=True)

    def __repr__(self):
        """ Function returns metadata when class is running to create database
        """
        return '<Package {}>'.format(self.id)