echo "The Average Length of Code in Question" >> report
echo "------------------------------------" >> report
#Retrieving the stats about the size of the answer code for language C++
FILES=$(pwd)/QCodeACode/C++/Question_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done


echo "C++ : `expr $sum / $total`" >> report

#Retrieving the stats about the size of the Question code for language Java
FILES=$(pwd)/QCodeACode/Java/Question_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "Java : `expr $sum / $total`" >> report

#Retrieving the stats about the size of the Question code for language C
FILES=$(pwd)/QCodeACode/C/Question_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "C : `expr $sum / $total`" >> report


#Retrieving the stats about the size of the Question code for language Python
FILES=$(pwd)/QCodeACode/Python/Question_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "Python : `expr $sum / $total`" >> report


echo "************************************" >> report
echo "The Average Length of Code in Answer" >> report
echo "------------------------------------" >> report
#Retrieving the stats about the size of the Answer code for language C++
FILES=$(pwd)/QCodeACode/C++/Answer_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done


echo "C++ : `expr $sum / $total`" >> report

#Retrieving the stats about the size of the answer code for language Java
FILES=$(pwd)/QCodeACode/Java/Answer_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "Java : `expr $sum / $total`" >> report

#Retrieving the stats about the size of the answer code for language C
FILES=$(pwd)/QCodeACode/C/Answer_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "C : `expr $sum / $total`" >> report


#Retrieving the stats about the size of the answer code for language Python
FILES=$(pwd)/QCodeACode/Python/Answer_Code/*
total=0
sum=0
for f in $FILES
do
  
  sum=`expr $sum + $(wc -l < $f)` >> report
  total=`expr $total + 1` >> report
done
echo "Python : `expr $sum / $total`" >> report

