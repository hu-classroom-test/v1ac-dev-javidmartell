# jupyter nbconvert --to script --ExecutePreprocessor.kernel_name=python3 --output code.py
rm -f code.py code0.py
jupyter nbconvert Analytical\ Computing.ipynb --to=script --output=code &&
sed -e '/Checkpoint 0/,$d' code.py \
    -e '/^\s*%/ d' \
    -e '/^\s*@/ d' \
    -e '/^\s*#/ d' \
     > code0.py 
cat test0.py >> code0.py &&
python code0.py
