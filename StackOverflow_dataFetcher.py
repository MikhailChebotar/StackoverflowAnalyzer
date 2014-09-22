import requests
import json
from pprint import pprint
import time
import re
import csv
from bs4 import BeautifulSoup as BSHTML


#update the info about the comments
def getCommentsInfo(f,code_text):
	count=0
	count = count + code_text.count("/*")
	count = count + code_text.count("//")
	count = count + code_text.count("#")
	if count > 0:
		f.write("Comments: Yes "+"\n")
	else:
		f.write("Comments: No "+"\n")

#Update the size of the code
def getCodeSize(f,code_text):
	count = code_text.count("\n")+1
	text = "CodeSize:"+str(count)+"\n"
	f.write(text)

#Update the number of Conditional Statements in the code
def getConditionalStatementInfo(f,code_text):
	count=code_text.count("if")
	text="Conditional: " + str(count)+"\n"
	f.write(text)

#Update the number of loops for the code
def getLoopInfo(f,code_text):
	count=0
	count = count+code_text.count("for")
	count = count + code_text.count("while")
	text="Loops: " + str(count) +"\n"
	f.write(text)

def parseQuestionCode(ques,curr_path,programming_Lang,code_text):
	#creating the report file
	ques_report_file="QuestionReport/"+str(ques['question_id'])+"_QR"+"_"+programming_Lang
	f = open(ques_report_file, "a+")
	getLoopInfo(f,code_text)
	getConditionalStatementInfo(f,code_text)
	getCodeSize(f,code_text)
	getCommentsInfo(f,code_text)
	f.close()

#Getting the  text from the answer Body
def storeAnswerText(ques,curr_path,programming_Lang):	
	answer_ID=1
	for ans in ques['answers']:
		BS = BSHTML(ans['body'])
		if BS.find_all('p'):
			ans_Text_File=curr_path+"Answer_Text/"+str(ques['question_id'])+"_AT"+str(answer_ID)+"_"+programming_Lang
			answer_ID=answer_ID+1
			f = open(ans_Text_File, "w")
			for segment in (BS.find_all('p')):
				codeText=str(segment.get_text().encode('utf8'))
				f.write(codeText)
			f.close()


#Getting the  text from the Question Body
def storeQuestionText(ques,curr_path,programming_Lang):
	ques_Text_File=curr_path+"Question_Text/"+str(ques['question_id'])+"_QT"+"_"+programming_Lang
	BS = BSHTML(ques['body'])
	f = open(ques_Text_File, "w")
	ques_Title=str(ques['title'].encode('utf8'))+"\n"+"----------"+"\n"
	f.write(ques_Title)
	for segment in BS.find_all('p'):
		#Storing the text in the file
		codeText=str(segment.get_text().encode('utf8'))
		f.write(codeText)

	f.close()

def storeQuestionCode(ques,curr_path,programming_Lang):
	#getting the code part from the user question body
	
	BS = BSHTML(ques['body'])
	ques_segment=1
	#codeText=str(BS.find_all('code'))
	
	EntireCodeText=" "
	for segment in BS.find_all('pre'):
		ques_Code_File=curr_path+"Question_Code/"+str(ques['question_id'])+"_QC_"+str(ques_segment)+"."+programming_Lang
		f = open(ques_Code_File, "w")
		ques_segment=ques_segment+1
		codeText=str(segment.get_text().encode('utf8'))
		EntireCodeText=EntireCodeText + codeText+"\n"
		#Storing the code text in the file
		f.write(codeText)
		f.close()

	parseQuestionCode(ques,curr_path,programming_Lang,EntireCodeText)

def storeAnswerCode(ques,curr_path,programming_Lang):
	answer_ID=1
	
	for ans in ques['answers']:
		BS = BSHTML(ans['body'])
		if BS.find_all('pre'):
			answer_ID=answer_ID+1
			ans_segment=1
			for segment in (BS.find_all('pre')):
				ans_Code_File=curr_path+"Answer_Code/"+str(ques['question_id'])+"_AC"+str(answer_ID)+"_"+str(ans_segment)+"."+programming_Lang
				f = open(ans_Code_File, "w")
				ans_segment=ans_segment+1
				codeText=str(segment.get_text().encode('utf8'))
				f.write(codeText)
				f.close()

#Question with Code and Answer with Code
def Category_Four(ques,programming_Lang):
	curr_path="QCodeACode/"+programming_Lang+"/"
	storeQuestionCode(ques,curr_path,programming_Lang,)
	storeQuestionText(ques,curr_path,programming_Lang)
	storeAnswerCode(ques,curr_path,programming_Lang)
	storeAnswerText(ques,curr_path,programming_Lang)
	
#Question with Code and Answer without code
def Category_Three(ques,programming_Lang):
	curr_path="QCodeA/"+programming_Lang+"/"
	storeQuestionCode(ques,curr_path,programming_Lang)
	storeQuestionText(ques,curr_path,programming_Lang)
	storeAnswerText(ques,curr_path,programming_Lang)

#Question without Code and Answer with Code
def Category_Two(ques,programming_Lang):
	curr_path="QACode/"+programming_Lang+"/"
	storeAnswerCode(ques,curr_path,programming_Lang)
	storeQuestionText(ques,curr_path,programming_Lang)
	storeAnswerText(ques,curr_path,programming_Lang)

#Question without Code and Answer without Code
def Category_One(ques,programming_Lang):
	curr_path="QA/"+programming_Lang+"/"
	storeAnswerText(ques,curr_path,programming_Lang)
	storeQuestionText(ques,curr_path,programming_Lang)
	

def processQuestions(questions,request_So_Far,programming_Lang):
	for q in questions:
		request_So_Far=request_So_Far+1
		qflag=False
		aflag=False
		if q['answer_count'] != 0:

			#Checking whether the question contains the code
			if q['body'].find('<code>') !=-1:
				qflag=True
			#Checking whether the answer contains the code
			for ans in q['answers']:
				if ans['body'].find('<code>')!=-1:
					aflag=True
					break
			if qflag and aflag:
				#Question with code and answer with code
				Category_Four(q,programming_Lang)

			elif qflag and (not aflag):
				#Question with code and answer without code
				Category_Three(q,programming_Lang)

			elif (not qflag) and aflag:
				#Question without code and answer with code
				Category_Two(q,programming_Lang)
			else:
				#Question without code and answer without code
				Category_One(q,programming_Lang)

def fetchQuestions(to_Date,period,programming_Lang):
	request_Limit=26000
	has_More=True
	request_So_Far=0
	while has_More and request_So_Far < request_Limit:
		request_So_Far=request_So_Far+1
		from_Date=to_Date-(86400*period)
		url="http://api.stackexchange.com/2.2/questions?pagesize=100&fromdate=%d&todate=%d&order=desc&tagged=%s&sort=votes&site=stackoverflow&filter=!-*7AsVmzB2CT" %(from_Date,to_Date,programming_Lang)
		r=requests.get(url)
		time.sleep(0.10)
		to_Date=from_Date
		response= r.json()
		questions= response['items']
		has_More=response['has_more']
		print response['quota_remaining']
		processQuestions(questions,request_So_Far,programming_Lang)
		print request_So_Far
		break

def main():
	#Calling the API to request
	to_Date=1401580700
	period=3
	programming_Lang="C++"
	fetchQuestions(to_Date,period,programming_Lang)


if __name__ == '__main__':
	main()