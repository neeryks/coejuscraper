if __name__=='__main__':
    import time
    from coeju import executer
    course,semester = input('Enter Course :'),input('Enter Semester :')
    while executer(course,semester) == 0:
       print('No Matching Result')
       time.sleep(1800)
    executer(course,semester)
    exit()
