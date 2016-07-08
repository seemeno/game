#coding = utf-8
import random

print ("has ")

def hello_world(str):
	print ("hello world " + str)
	return 

class Puzzle:
	__puzzleList = []
	
	__len = 4
	
	def __init__(self):
		self.refresh();
		return	
		
	'''	
	def __del__(self):
		del self.__puzzleList
		del self.__len
		return
	'''	
	
	def refresh(self):
		self.__clear()
		for index in range(self.__len * self.__len - 1):
			self.__puzzleList.append(index+1)
		random.shuffle(self.__puzzleList)
		self.__puzzleList.append(0);
		return
	
	def __clear(self):
		while len(self.__puzzleList) != 0:
			self.__puzzleList.pop()
	
	def __str__(self):
		string = ""
		for index in range(len(self.__puzzleList)):
			if 0 != index and 0 == index % self.__len:
				string += "\n"
			if 0 == self.__puzzleList[index]:
				string += " ".center(4)
				#rjust or ljust
			else:
				string += str(self.__puzzleList[index]).center(4)
		return string
	
	def move_block(self,siteX,siteY):
		site = (siteX-1) * self.__len + siteY - 1
		is_move = True
		if siteY < 1 or siteY > self.__len or siteX > self.__len or siteX < 1:
			is_move = False
		elif siteY != self.__len and 0 == self.__puzzleList[site + 1]:
			self.__puzzleList[site + 1] = self.__puzzleList[site]
			self.__puzzleList[site] = 0
		elif siteY != 1 and 0 == self.__puzzleList[site - 1]:
			self.__puzzleList[site - 1] = self.__puzzleList[site]
			self.__puzzleList[site] = 0
		elif siteX != 1 and 0 == self.__puzzleList[site - self.__len]:
			self.__puzzleList[site - self.__len] = self.__puzzleList[site]
			self.__puzzleList[site] = 0
		elif siteX != self.__len and 0 == self.__puzzleList[site + self.__len]:
			self.__puzzleList[site + self.__len] = self.__puzzleList[site]
			self.__puzzleList[site] = 0
		else:
			is_move = False
		return is_move
		
	def if_finished(self):
		for index in range(len(self.__puzzleList)):
			if index + 1 != self.__puzzleList[index]:
				return False
		return True
	

