import manager

man = manager.Manager()
man.create_new_test()
man.current_test.add('QstEnterText')
man.current_test.add('QstTable')
man.current_test.workTestFile()
man.current_test.passingTest()
man.current_test.passingTest()
man.current_test.workAnswerFile()
#man.delete()
