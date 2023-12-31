import src.lambda_transformation.utils.dim_staff as util
import src.lambda_transformation.utils.get_tables as tables
from pandas import DataFrame


def test_timestamp_is_preserved():
    try:
        staff = tables.read_table('staff.csv')
        depts = tables.read_table('department.csv')
        result = util.staff_department_to_dim_staff(staff, depts)
        # Get the most recent timestamp
        recent_timestamp = [
            staff['Timestamp'],
            depts['Timestamp']
        ]
        result_timestamp = result['Timestamp']

        # Are the timestamps the same?
        assert recent_timestamp[0] == recent_timestamp[1]

        # Is the timestamp of the result correct?
        assert result_timestamp == recent_timestamp[0]

    except tables.TableNotFoundError:
        pass


def test_body_is_a_pd_dataframe():
    try:
        result: DataFrame = util.staff_department_to_dim_staff(
            tables.read_table('staff.csv'),
            tables.read_table('department.csv')
        )
        assert type(result['Body']) is DataFrame
    except tables.TableNotFoundError:
        pass


def test_body_is_as_expected():
    try:
        staff = tables.read_table('staff.csv')
        depts = tables.read_table('department.csv')
        result = util.staff_department_to_dim_staff(staff, depts)

        body = result['Body']

        '''
            As according to the schema
        '''

        expected_columns = [
            'staff_id',
            'first_name',
            'last_name',
            'department_name',
            'location',
            'email_address'
        ]

        for column in expected_columns:
            assert column in body.columns
    except tables.TableNotFoundError:
        pass
