import test

test1 = test.Test('How are you doing', 'Something about information you may know')
test1.createAnswerFile()
test1.add('QstEnterText')
test1.add('QstTrueFalse')
test1.add('QstEnterText')
test1.add('QstOneAnswer')
test1.workTestFile()
test1.passingTest()
