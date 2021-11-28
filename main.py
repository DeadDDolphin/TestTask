from user_collection import UserCollection


if __name__ == '__main__':
    # create instance of UserCollection
    obj = UserCollection()
    # read and create the users
    obj.read_users()
    # write reports to files
    obj.write_users()
