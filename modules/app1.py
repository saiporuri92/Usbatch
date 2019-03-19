'''
import folder1
folder1.file2.fun()
'''
'''
from folder1 import file1,file2
file1.fun()
file2.fun()

import folder1
folder1.file1.fun()

import folder1
folder1.file1.fun()
'''
from folder1 import file1
file1.fun()

#if __name__ == "__main__"