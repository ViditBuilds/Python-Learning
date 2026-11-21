# pyright: reportMissingImports=false
# =====================================================================
#   QUIZ GENERATOR PROJECT  (Single File)
#   Run karne ke liye: python quiz_generator_project.py
#   Zaroori: pip install pandas numpy
# =====================================================================

import os  # file path aur file check ke liye
import sys  # modules register karne ke liye
import types  # naye modules banane ke liye
import numpy as np  # NumPy
import pandas as pd  # Pandas

# =====================================================================
# SECTION 1: DATASET (60 records) - Python list of tuples
# Format: (question, option1, option2, option3, option4, answer, category, difficulty)
# Kuch records mein difficulty jaan-bujhkar khaali ("") hai -> missing values demo
# =====================================================================
QUESTIONS = [
    ('Python ka creator kaun hai?', 'Linus Torvalds', 'Elon Musk', 'Guido van Rossum', 'Bill Gates', 3, 'Python Basics', 'Easy'),
    ('Python file ka extension kya hota hai?', '.java', '.html', '.cpp', '.py', 4, 'Python Basics', 'Easy'),
    ('print() function ka kaam kya hai?', 'File delete karna', 'Input lena', 'Loop chalana', 'Output dikhana', 4, 'Python Basics', 'Easy'),
    ('Python mein comment kis symbol se likhte hain?', '--', '/*', '//', '#', 4, 'Python Basics', 'Easy'),
    ('type(5) ka output kya hoga?', 'int', 'str', 'float', 'bool', 1, 'Python Basics', ''),
    ('10 // 3 ka result kya hai?', '4', '1', '3.33', '3', 4, 'Python Basics', 'Easy'),
    ('2 ** 3 ka result kya hai?', '5', '9', '8', '6', 3, 'Python Basics', 'Easy'),
    ('input() function hamesha kya return karta hai?', 'list', 'int', 'string', 'float', 3, 'Python Basics', 'Medium'),
    ("len('Python') ka output kya hai?", '6', '7', '5', '4', 1, 'Python Basics', 'Easy'),
    ('Python case-sensitive language hai?', 'Nahi', 'Sirf functions mein', 'Sirf variables mein', 'Haan', 4, 'Python Basics', 'Easy'),
    ('Python mein loop ke liye kaunsa keyword use hota hai?', 'cycle', 'repeat', 'for', 'loopit', 3, 'Python Basics', 'Easy'),
    ('bool(0) ka output kya hoga?', 'Error', 'False', 'None', 'True', 2, 'Python Basics', 'Medium'),
    ('List kis bracket se banti hai?', '<>', '{}', '()', '[]', 4, 'Data Structures', 'Easy'),
    ('Tuple kis bracket se banta hai?', '[]', '<>', '()', '{}', 3, 'Data Structures', 'Easy'),
    ('Dictionary (key:value) kis bracket se banti hai?', '[]', '<>', '{}', '()', 3, 'Data Structures', 'Easy'),
    ('Inme se kaunsa immutable hai?', 'list', 'dict', 'tuple', 'set', 3, 'Data Structures', 'Medium'),
    ('Set mein duplicate values ka kya hota hai?', 'Allowed hain', 'Error aata hai', 'Automatically hat jaati hain', 'Sirf numbers allowed', 3, 'Data Structures', ''),
    ('List ke end mein element add karne ka method?', 'push()', 'append()', 'add()', 'insert_end()', 2, 'Data Structures', 'Easy'),
    ('list.pop() kya karta hai?', 'List sort karta hai', 'Last element hata ke return karta hai', 'List clear karta hai', 'Pehla element dikhata hai', 2, 'Data Structures', 'Medium'),
    ('Dictionary ke saare keys kaise milenge?', 'names()', 'getkeys()', 'allkeys()', 'keys()', 4, 'Data Structures', 'Medium'),
    ('List ko sort karne ka method kaunsa hai?', 'order()', 'arrange()', 'sort()', 'sorted_list()', 3, 'Data Structures', 'Easy'),
    ('t = (1,2,3); t[0] = 5 likhne par kya hoga?', 'TypeError aayega', 'Value badal jayegi', 'Tuple list ban jayega', 'NameError aayega', 1, 'Data Structures', 'Hard'),
    ('len(set([1,1,2,2,3])) ka answer kya hai?', '1', '3', '2', '5', 2, 'Data Structures', 'Medium'),
    ("dict.get('x') agar key 'x' nahi hai to kya milega?", '0', 'KeyError', 'False', 'None', 4, 'Data Structures', 'Hard'),
    ('Function define karne ka keyword kaunsa hai?', 'func', 'function', 'def', 'define', 3, 'Functions & Modules', 'Easy'),
    ('Function se value wapas bhejne ka keyword?', 'output', 'return', 'send', 'give', 2, 'Functions & Modules', 'Easy'),
    ('Module import karne ka keyword kaunsa hai?', 'include', 'import', 'require', 'using', 2, 'Functions & Modules', 'Easy'),
    ('lambda kya hota hai?', 'Loop', 'Anonymous function', 'Class', 'Module', 2, 'Functions & Modules', 'Medium'),
    ('*args ka use kya hai?', 'Class banane ke liye', 'Keyword arguments ke liye', 'Loop chalane ke liye', 'Variable number of positional arguments lene ke liye', 4, 'Functions & Modules', 'Hard'),
    ("if __name__ == '__main__' kya check karta hai?", 'File delete ho rahi hai ya nahi', 'File direct run ho rahi hai ya nahi', 'Module import hua ya nahi', 'Error aaya ya nahi', 2, 'Functions & Modules', 'Hard'),
    ('def f(x=5) mein f() call karne par x kya hoga?', '0', '5', 'None', 'Error', 2, 'Functions & Modules', 'Medium'),
    ('pip ka use kisliye hota hai?', 'Python packages install karne ke liye', 'Debug karne ke liye', 'Code run karne ke liye', 'Compile karne ke liye', 1, 'Functions & Modules', 'Easy'),
    ('math.sqrt(16) ka output kya hai?', 'Error', '8', '4.0', '256', 3, 'Functions & Modules', ''),
    ('random.shuffle() kya karta hai?', 'List sort karta hai', 'List reverse karta hai', 'List ko shuffle karta hai', 'List delete karta hai', 3, 'Functions & Modules', 'Medium'),
    ('NumPy ka full form kya hai?', 'New Python', 'Number Pad', 'Numerical Python', 'Network Python', 3, 'NumPy', 'Easy'),
    ('NumPy ko import karte waqt common alias kya hai?', 'nm', 'py', 'np', 'numpy', 3, 'NumPy', 'Easy'),
    ('1D array banane ke liye kaunsa function hai?', 'np.array([1,2,3])', 'np.make([1,2,3])', 'np.list([1,2,3])', 'np.new([1,2,3])', 1, 'NumPy', 'Easy'),
    ('arr.shape kya batata hai?', 'Mean', 'Sum', 'Data type', 'Array ki dimensions/size', 4, 'NumPy', 'Medium'),
    ('np.mean() kya nikalta hai?', 'Average', 'Sum', 'Maximum', 'Minimum', 1, 'NumPy', 'Easy'),
    ('np.std() kya calculate karta hai?', 'Standard deviation', 'Median', 'Mode', 'Sum', 1, 'NumPy', 'Medium'),
    ('arr[1:3] kaunse elements dega?', 'Index 1 aur 2', 'Index 0 se 3', 'Index 1, 2 aur 3', 'Sirf index 3', 1, 'NumPy', 'Medium'),
    ('2D array ke element ko access karne ka tarika?', 'arr<0,1>', 'arr{0,1}', 'arr[0,1]', 'arr(0,1)', 3, 'NumPy', 'Medium'),
    ('np.zeros((2,3)) ki shape kya hogi?', '(2,)', '(6,)', '(3,2)', '(2,3)', 4, 'NumPy', 'Medium'),
    ('np.arange(0,5) kya dega?', '[1 2 3 4 5]', '[1 2 3 4]', '[0 1 2 3 4]', '[0 1 2 3 4 5]', 3, 'NumPy', 'Medium'),
    ('np.max() kya return karta hai?', 'Maximum value', 'Mean', 'Sum', 'Minimum value', 1, 'NumPy', 'Easy'),
    ('List aur NumPy array mein kaun fast hota hai?', 'Dono same', 'NumPy array', 'Tuple', 'List', 2, 'NumPy', 'Medium'),
    ('Pandas ka main 2D data structure kaunsa hai?', 'DataFrame', 'Tuple', 'Stack', 'Set', 1, 'Pandas', 'Easy'),
    ('CSV file read karne ka function kaunsa hai?', 'pd.csv()', 'pd.read_csv()', 'pd.load()', 'pd.open_csv()', 2, 'Pandas', 'Easy'),
    ('df.head() kya dikhata hai?', 'Pehli 5 rows', 'Aakhri 5 rows', 'Columns', 'Shape', 1, 'Pandas', 'Easy'),
    ('df.tail() kya dikhata hai?', 'Pehli 5 rows', 'Columns', 'Aakhri 5 rows', 'Info', 3, 'Pandas', 'Easy'),
    ('Missing values count karne ka tarika?', 'df.empty()', 'df.nan()', 'df.missing()', 'df.isnull().sum()', 4, 'Pandas', 'Medium'),
    ('Missing values bharne ka method kaunsa hai?', 'fill()', 'replace_na()', 'addna()', 'fillna()', 4, 'Pandas', ''),
    ('DataFrame ko sort karne ka method?', 'sort()', 'sort_values()', 'arrange()', 'order()', 2, 'Pandas', 'Medium'),
    ('Pandas mein group karke calculation ka method?', 'cluster()', 'combine()', 'group()', 'groupby()', 4, 'Pandas', 'Medium'),
    ('df.describe() kya deta hai?', 'Rows delete karta hai', 'Sort karta hai', 'Plot banata hai', 'Statistical summary', 4, 'Pandas', 'Medium'),
    ('DataFrame se row/column hatane ka method?', 'df.delete()', 'df.cut()', 'df.remove()', 'df.drop()', 4, 'Pandas', 'Medium'),
    ('df.loc kis par based selection karta hai?', 'Sirf sorting', 'Sirf loop', 'Sirf merge', 'Labels (naam)', 4, 'Pandas', 'Hard'),
    ('df.iloc kis par based selection karta hai?', 'Integer position', 'Deleting', 'Sorting', 'Labels', 1, 'Pandas', 'Hard'),
    ('Excel file read karne ka function kaunsa hai?', 'pd.read_excel()', 'pd.excel()', 'pd.xls()', 'pd.open_xls()', 1, 'Pandas', 'Easy'),
    ('df.shape kya return karta hai?', 'Sum', 'Mean', '(rows, columns)', 'Data type', 3, 'Pandas', 'Easy'),
]

# =====================================================================
# SECTION 2: PYTHON MODULES (3 modules) - code ke andar hi create honge
# Har module ka source code ek string mein hai, phir create_module() se
# asli module banta hai aur uske baad normal "import" se import hota hai.
# =====================================================================

# ---------- MODULE 1: helpers (chhote helper functions) ----------
HELPERS_CODE = r'''
def print_header(title):  # heading dikhane ka function
    print("\n" + "=" * 70)  # upar ki line
    print(title.center(70))  # title ko beech mein rakho
    print("=" * 70)  # neeche ki line


def ask_text(prompt):  # khaali nahi hona chahiye wala text input
    while True:  # sahi input milne tak loop
        value = input(prompt).strip()  # input lo aur extra space hatao
        if value:  # agar kuch likha hai
            return value  # wahi wapas bhejo
        print("Khaali input nahi chalega, dobara try karo.")  # warning


def ask_int(prompt, low, high):  # range ke andar number input
    while True:  # sahi number milne tak loop
        try:  # error handling shuru
            number = int(input(prompt))  # text ko number banao
            if low <= number <= high:  # range check
                return number  # sahi number wapas bhejo
            print(f"{low} se {high} ke beech number daalo.")  # range ka message
        except ValueError:  # agar number nahi tha
            print("Number daalo, text nahi.")  # error message


def show_record(row):  # ek question ki poori detail dikhao
    print(f"\nID         : {row['id']}")  # id
    print(f"Question   : {row['question']}")  # question
    for i in range(1, 5):  # 4 options ke liye loop
        key = f"option{i}"  # column ka naam banao
        print(f"  Option {i} : {row[key]}")  # option dikhao
    print(f"Sahi Answer: Option {row['answer']}")  # sahi option number
    print(f"Category   : {row['category']}")  # category
    print(f"Difficulty : {row['difficulty']}  (Marks: {row['marks']})")  # difficulty aur marks
'''

# ---------- MODULE 2: datastore (file handling + data load/save) ----------
DATASTORE_CODE = r'''
import os  # file check ke liye
import csv  # CSV likhne ke liye
import pandas as pd  # CSV padhne ke liye

# Tuple: categories fixed hain, isliye tuple (immutable)
CATEGORIES = ("Python Basics", "Data Structures", "Functions & Modules", "NumPy", "Pandas")

# Dictionary: difficulty -> marks mapping
DIFFICULTY_MARKS = {"Easy": 1, "Medium": 2, "Hard": 3}

# CSV file ka path (main file isse set karti hai)
FILE_PATH = "quiz_data.csv"

# CSV ke column names (list)
COLUMNS = ["id", "question", "option1", "option2", "option3", "option4",
           "answer", "category", "difficulty", "marks"]


def create_dataset_if_missing(questions):  # CSV nahi hai to bana do (file handling)
    if os.path.exists(FILE_PATH):  # agar file pehle se hai
        return  # kuch mat karo
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:  # file likhne ke liye kholo
        writer = csv.writer(f)  # CSV writer
        writer.writerow(COLUMNS)  # header row
        for number, q in enumerate(questions, start=1):  # har question ke liye
            marks = DIFFICULTY_MARKS.get(q[7], "")  # difficulty se marks (khaali ho to khaali)
            writer.writerow([number, *q, marks])  # ek row likho
    print(f"[Info] Dataset file ban gayi: {FILE_PATH}")  # info


def handle_missing(df):  # missing values handle karne ka function
    missing = int(df.isnull().sum().sum())  # kul missing values count
    df["difficulty"] = df["difficulty"].fillna("Medium")  # khaali difficulty = Medium
    df["marks"] = df["difficulty"].map(DIFFICULTY_MARKS).astype(int)  # marks dobara banao
    if missing > 0:  # agar missing mili
        print(f"[Info] {missing} missing values mili aur fix kar di gayi.")  # batao
    return df  # saaf DataFrame wapas


def load_data():  # CSV se data load karo
    df = pd.read_csv(FILE_PATH, keep_default_na=False, na_values=[""])  # sirf khaali cell = missing
    return handle_missing(df)  # missing fix karke bhejo


def save_data(df):  # DataFrame ko CSV mein save karo
    df.to_csv(FILE_PATH, index=False)  # bina index ke likho


def get_next_id(df):  # naya unique id banao
    if df.empty:  # agar data khaali hai
        return 1  # pehla id 1
    return int(df["id"].max()) + 1  # sabse bada id + 1


def file_info():  # open() se raw file padho aur info nikalo
    with open(FILE_PATH, "r", encoding="utf-8") as f:  # file kholo
        lines = f.readlines()  # saari lines list mein lo
    size_kb = os.path.getsize(FILE_PATH) / 1024  # file size KB mein
    return {"lines": len(lines), "size_kb": round(size_kb, 2)}  # dictionary return
'''

# ---------- MODULE 3: analysis (NumPy + Pandas + report) ----------
ANALYSIS_CODE = r'''
import numpy as np  # NumPy
import pandas as pd  # Pandas
import helpers  # module 1 ko import kiya
import datastore  # module 2 ko import kiya


def numpy_analysis(df):  # NumPy ke saare concepts
    helpers.print_header("NUMPY ANALYSIS")  # heading

    arr_1d = np.array(df["marks"])  # 1D array: saare questions ke marks
    arr_2d = np.array(df[["id", "answer", "marks"]])  # 2D array: id, answer, marks
    print("1D array (pehle 10 marks):", arr_1d[:10])  # 1D ka ek hissa
    print("2D array shape (rows, cols):", arr_2d.shape)  # 2D ki shape

    print("\n--- Indexing & Slicing ---")  # sub heading
    print("Pehla element arr_1d[0]      :", arr_1d[0])  # indexing
    print("Last element arr_1d[-1]      :", arr_1d[-1])  # negative indexing
    print("Slice arr_1d[5:10]           :", arr_1d[5:10])  # slicing
    print("2D element arr_2d[0, 2]      :", arr_2d[0, 2])  # 2D indexing
    print("2D pehli 3 rows:\n", arr_2d[:3])  # row slicing
    print("2D 'answer' column (pehle 5) :", arr_2d[:5, 1])  # column slicing

    print("\n--- Statistics on Marks ---")  # sub heading
    print("Sum (total marks)      :", np.sum(arr_1d))  # sum
    print("Mean (average)         :", round(float(np.mean(arr_1d)), 2))  # mean
    print("Maximum                :", np.max(arr_1d))  # max
    print("Minimum                :", np.min(arr_1d))  # min
    print("Standard Deviation     :", round(float(np.std(arr_1d)), 2))  # std

    print("\n--- Sahi option ka distribution ---")  # sub heading
    counts = np.bincount(np.array(df["answer"]), minlength=5)[1:]  # option 1-4 ki ginti
    for option, count in enumerate(counts, start=1):  # har option ke liye
        print(f"Option {option} sahi answer hai: {count} questions mein")  # print


def pandas_analysis(df):  # Pandas ke saare concepts
    helpers.print_header("PANDAS ANALYSIS")  # heading

    print("--- DataFrame ka Shape ---")  # sub heading
    print("Rows, Columns:", df.shape)  # shape

    print("\n--- Selected rows & columns (loc) ---")  # sub heading
    print(df.loc[0:4, ["id", "category", "difficulty"]].to_string(index=False))  # label based

    print("\n--- Selected rows (iloc) ---")  # sub heading
    print(df.iloc[10:14, [0, 7]].to_string(index=False))  # position based

    print("\n--- Filtering: Hard questions ---")  # sub heading
    hard = df[df["difficulty"] == "Hard"]  # filter
    print(f"Hard questions: {len(hard)}")  # count
    print(hard[["id", "category", "marks"]].head(5).to_string(index=False))  # pehle 5

    print("\n--- Filtering: NumPy category + marks >= 2 ---")  # sub heading
    combo = df[(df["category"] == "NumPy") & (df["marks"] >= 2)]  # do conditions
    print(f"Matching questions: {len(combo)}")  # count

    print("\n--- Sorting: marks (zyada se kam), phir id ---")  # sub heading
    sorted_df = df.sort_values(by=["marks", "id"], ascending=[False, True])  # sort
    print(sorted_df[["id", "category", "difficulty", "marks"]].head(5).to_string(index=False))  # top 5

    print("\n--- GroupBy: Category wise ---")  # sub heading
    by_cat = df.groupby("category").agg(  # category se group
        questions=("id", "count"),  # kitne questions
        avg_marks=("marks", "mean"),  # average marks
        total_marks=("marks", "sum"),  # total marks
    ).round(2)  # 2 decimal
    print(by_cat)  # table

    print("\n--- GroupBy: Difficulty wise ---")  # sub heading
    print(df.groupby("difficulty")["id"].count())  # difficulty wise count

    print("\n--- Missing Values (raw CSV file mein) ---")  # sub heading
    raw = pd.read_csv(datastore.FILE_PATH, keep_default_na=False, na_values=[""])  # raw file padho
    missing_counts = raw.isnull().sum()  # har column ke missing
    if missing_counts.sum() > 0:  # agar missing hain
        print(missing_counts[missing_counts > 0].to_string())  # sirf jahan missing hai
    else:  # nahi hain
        print("Koi missing value nahi (pehle hi fix hokar save ho chuki hain).")  # message
    print("Fix ke baad missing:", int(df.isnull().sum().sum()))  # loaded data mein 0

    print("\n--- Statistical Analysis (describe) ---")  # sub heading
    print(df[["marks", "answer"]].describe().round(2))  # stats table


def summary_report(df):  # poori summary report
    helpers.print_header("SUMMARY REPORT")  # heading
    info = datastore.file_info()  # file ki info (open() se)
    marks = np.array(df["marks"])  # marks array
    print(f"Dataset file     : quiz_data.csv ({info['lines']} lines, {info['size_kb']} KB)")  # file info
    print(f"Total questions  : {len(df)}")  # total
    print(f"Total categories : {df['category'].nunique()}")  # unique categories
    print(f"Total marks      : {int(np.sum(marks))}")  # sum
    print(f"Average marks    : {np.mean(marks):.2f}")  # mean
    print(f"Marks std. dev.  : {np.std(marks):.2f}")  # standard deviation

    print("\nCategory wise questions:")  # sub heading
    print(df["category"].value_counts().to_string())  # counts

    print("\nDifficulty wise questions:")  # sub heading
    print(df["difficulty"].value_counts().to_string())  # counts

    print("\n--- Insights ---")  # sub heading
    top_cat = df["category"].value_counts().idxmax()  # sabse zyada questions wali category
    hard_pct = (df["difficulty"] == "Hard").mean() * 100  # Hard ka percentage
    easy_pct = (df["difficulty"] == "Easy").mean() * 100  # Easy ka percentage
    tough_cat = df.groupby("category")["marks"].mean().idxmax()  # sabse tough category
    common = int(np.bincount(np.array(df["answer"])).argmax())  # sabse common sahi option
    print(f"1. Sabse zyada questions '{top_cat}' category mein hain.")  # insight 1
    print(f"2. Easy {easy_pct:.1f}% aur Hard {hard_pct:.1f}% questions hain.")  # insight 2
    print(f"3. Average marks ke hisaab se sabse tough category: '{tough_cat}'.")  # insight 3
    print(f"4. Sabse zyada sahi answer Option {common} hai.")  # insight 4
'''


def create_module(name, source):  # string se asli module banane ka function
    module = types.ModuleType(name)  # khaali module object
    sys.modules[name] = module  # Python ko batao ki ye module maujood hai
    exec(source, module.__dict__)  # source code module ke andar chalao
    return module  # module wapas


# Modules banao (order important hai: analysis, helpers aur datastore par depend karta hai)
create_module("helpers", HELPERS_CODE)  # module 1 create
datastore_module = create_module("datastore", DATASTORE_CODE)  # module 2 create
setattr(datastore_module, "FILE_PATH", os.path.join(  # CSV ka path isi file ke folder mein set karo
    os.path.dirname(os.path.abspath(__file__)), "quiz_data.csv"))
create_module("analysis", ANALYSIS_CODE)  # module 3 create

# Ab modules ko normal tareeke se IMPORT karo
import helpers  # type: ignore  # module 1 import
import datastore  # type: ignore  # module 2 import
import analysis  # type: ignore  # module 3 import
from helpers import print_header, ask_text, ask_int, show_record  # type: ignore  # helpers ke functions
from datastore import CATEGORIES, DIFFICULTY_MARKS, save_data, get_next_id, load_data  # type: ignore  # datastore ke functions


# =====================================================================
# SECTION 3: PROJECT FUNCTIONS (Add / Display / Search / Update / Delete)
# =====================================================================

def pick_category():  # category chunne ka function
    for i, cat in enumerate(CATEGORIES, start=1):  # tuple ko number ke saath dikhao
        print(f"  {i}. {cat}")  # category print
    choice = ask_int("Category number: ", 1, len(CATEGORIES))  # user ka choice
    return CATEGORIES[choice - 1]  # category ka naam wapas


def pick_difficulty():  # difficulty chunne ka function
    levels = list(DIFFICULTY_MARKS.keys())  # dict ke keys ko list banao
    for i, level in enumerate(levels, start=1):  # levels dikhao
        print(f"  {i}. {level}")  # level print
    choice = ask_int("Difficulty number: ", 1, len(levels))  # user ka choice
    return levels[choice - 1]  # difficulty ka naam wapas


def display_all(df):  # saare records table mein dikhao
    print_header(f"SAARE QUESTIONS (Total: {len(df)})")  # heading
    view = df[["id", "question", "category", "difficulty", "marks"]].copy()  # sirf zaroori columns
    view["question"] = view["question"].str[:45]  # lamba question chhota karo
    print(view.to_string(index=False))  # table print


def search_record(df):  # record search karo
    print_header("QUESTION SEARCH")  # heading
    keyword = ask_text("Keyword ya category likho (jaise numpy): ")  # search word
    in_question = df["question"].str.contains(keyword, case=False, na=False, regex=False)  # question mein
    in_category = df["category"].str.contains(keyword, case=False, na=False, regex=False)  # category mein
    result = df[in_question | in_category]  # dono mein se koi bhi match
    if result.empty:  # kuch nahi mila
        print("Koi record nahi mila.")  # message
        return  # function khatam
    print(f"\n{len(result)} record(s) mile:")  # kitne mile
    for _, row in result.head(5).iterrows():  # pehle 5 dikhao
        show_record(row)  # poori detail
    if len(result) > 5:  # agar zyada hain
        print(f"\n... aur {len(result) - 5} records. Keyword aur specific karo.")  # hint


def add_record(df):  # naya record add karo
    print_header("NAYA QUESTION ADD KARO")  # heading
    question = ask_text("Question: ")  # question lo
    options = []  # options ki khaali list
    for i in range(1, 5):  # 4 options ke liye loop
        options.append(ask_text(f"Option {i}: "))  # list mein append
    answer = ask_int("Sahi option number (1-4): ", 1, 4)  # sahi answer
    category = pick_category()  # category chuno
    difficulty = pick_difficulty()  # difficulty chuno
    record = {"id": get_next_id(df), "question": question}  # dictionary banao
    record.update({f"option{i}": opt for i, opt in enumerate(options, start=1)})  # options add karo
    record.update({"answer": answer, "category": category,  # baaki fields add karo
                   "difficulty": difficulty, "marks": DIFFICULTY_MARKS[difficulty]})
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)  # nayi row jodo
    save_data(df)  # CSV mein save
    print(f"\nQuestion add ho gaya! (ID: {record['id']})")  # confirmation
    return df  # updated DataFrame wapas


def update_record(df):  # purana record update karo
    print_header("QUESTION UPDATE KARO")  # heading
    record_id = ask_int("Update karne wala ID: ", 1, 999999)  # id lo
    mask = df["id"] == record_id  # us id wali row ka filter
    if not mask.any():  # id nahi mili
        print("Ye ID nahi mili.")  # message
        return df  # bina change wapas
    show_record(df[mask].iloc[0])  # purana record dikhao
    fields = ["question", "option1", "option2", "option3", "option4",  # editable fields ki list
              "answer", "category", "difficulty"]
    print("\nKya update karna hai?")  # poochho
    for i, field in enumerate(fields, start=1):  # fields dikhao
        print(f"  {i}. {field}")  # field print
    field = fields[ask_int("Field number: ", 1, len(fields)) - 1]  # field chuno
    if field == "answer":  # agar answer badalna hai
        value = ask_int("Naya sahi option (1-4): ", 1, 4)  # number lo
    elif field == "category":  # agar category badalni hai
        value = pick_category()  # category chuno
    elif field == "difficulty":  # agar difficulty badalni hai
        value = pick_difficulty()  # difficulty chuno
        df.loc[mask, "marks"] = DIFFICULTY_MARKS[value]  # marks bhi update karo
    else:  # baaki text fields
        value = ask_text("Nayi value: ")  # text lo
    df.loc[mask, field] = value  # value update karo
    save_data(df)  # CSV mein save
    print("\nRecord update ho gaya!")  # confirmation
    show_record(df[mask].iloc[0])  # naya record dikhao
    return df  # updated DataFrame wapas


def delete_record(df):  # record delete karo
    print_header("QUESTION DELETE KARO")  # heading
    record_id = ask_int("Delete karne wala ID: ", 1, 999999)  # id lo
    mask = df["id"] == record_id  # us id ka filter
    if not mask.any():  # id nahi mili
        print("Ye ID nahi mili.")  # message
        return df  # bina change wapas
    show_record(df[mask].iloc[0])  # record dikhao
    sure = input("\nPakka delete karna hai? (y/n): ").strip().lower()  # confirm
    if sure != "y":  # agar y nahi
        print("Delete cancel.")  # message
        return df  # bina change wapas
    df = df[~mask].reset_index(drop=True)  # us row ko hatao
    save_data(df)  # CSV mein save
    print("Record delete ho gaya!")  # confirmation
    return df  # updated DataFrame wapas


# =====================================================================
# SECTION 4: QUIZ GAME
# =====================================================================

def choose_category(df):  # quiz ke liye category chunne ka function
    categories = sorted(set(df["category"]))  # Set se unique categories, phir sorted list
    print("\nCategories:")  # heading
    print("  0. Sab categories (mixed)")  # mixed option
    for i, cat in enumerate(categories, start=1):  # categories dikhao
        print(f"  {i}. {cat}")  # print
    choice = ask_int("Category chuno: ", 0, len(categories))  # choice lo
    return None if choice == 0 else categories[choice - 1]  # None = sab


def play_quiz(df):  # quiz chalao
    print_header("QUIZ KHELO")  # heading
    category = choose_category(df)  # category chuno
    pool = df if category is None else df[df["category"] == category]  # questions ka pool
    total = ask_int(f"Kitne questions? (1-{len(pool)}): ", 1, len(pool))  # kitne chahiye
    selected = pool.sample(n=total)  # random questions chuno

    score = 0  # sahi answers
    marks_earned = 0  # kamaye hue marks
    wrong = []  # galat questions ki list
    stats = {}  # dictionary: category -> [sahi, total]

    for number, (_, row) in enumerate(selected.iterrows(), start=1):  # har question ke liye
        print(f"\nQ{number}. {row['question']}  [{row['category']} | {row['difficulty']}]")  # question
        for i in range(1, 5):  # options dikhao
            text = row[f"option{i}"]  # option ka text
            print(f"   {i}. {text}")  # print
        choice = ask_int("Aapka answer (1-4): ", 1, 4)  # answer lo
        stats.setdefault(row["category"], [0, 0])  # category ka entry banao
        stats[row["category"]][1] += 1  # total badhao
        if choice == row["answer"]:  # sahi answer
            print("Sahi jawab!")  # message
            score += 1  # score badhao
            marks_earned += int(row["marks"])  # marks jodo
            stats[row["category"]][0] += 1  # category ka sahi badhao
        else:  # galat answer
            correct = row[f"option{row['answer']}"]  # sahi option ka text
            print(f"Galat! Sahi jawab: {correct}")  # sahi batao
            wrong.append((row["question"], correct))  # tuple list mein append

    result = (score, total, marks_earned)  # Tuple: final result
    max_marks = int(selected["marks"].sum())  # maximum possible marks
    print_header("QUIZ RESULT")  # heading
    print(f"Score : {result[0]}/{result[1]}")  # score
    print(f"Marks : {result[2]}/{max_marks}")  # marks
    print(f"Percentage: {result[0] / result[1] * 100:.1f}%")  # percentage

    print("\nCategory wise performance:")  # sub heading
    for cat, (right, count) in stats.items():  # dictionary ke items
        print(f"  {cat:<22} {right}/{count}")  # print

    if wrong:  # agar galat answers hain
        print("\nYe questions dobara dekho:")  # heading
        for question, correct in wrong:  # har galat question
            print(f"  - {question} -> {correct}")  # print


# =====================================================================
# SECTION 5: MAIN MENU
# =====================================================================

def show_menu():  # menu dikhane ka function
    print_header("QUIZ GENERATOR - MAIN MENU")  # heading
    print("  1. Saare questions dikhao")  # option 1
    print("  2. Question search karo")  # option 2
    print("  3. Naya question add karo")  # option 3
    print("  4. Question update karo")  # option 4
    print("  5. Question delete karo")  # option 5
    print("  6. Quiz khelo")  # option 6
    print("  7. Summary report")  # option 7
    print("  8. NumPy analysis")  # option 8
    print("  9. Pandas analysis")  # option 9
    print("  0. Exit")  # exit


def main():  # program ka main function
    datastore.create_dataset_if_missing(QUESTIONS)  # CSV nahi hai to bana do
    df = load_data()  # dataset load karo
    print(f"Dataset load ho gaya: {len(df)} questions.")  # info
    while True:  # menu baar baar dikhao
        show_menu()  # menu print
        choice = input("\nApna choice daalo (0-9): ").strip()  # choice lo
        if choice == "1":  # display
            display_all(df)
        elif choice == "2":  # search
            search_record(df)
        elif choice == "3":  # add
            df = add_record(df)
        elif choice == "4":  # update
            df = update_record(df)
        elif choice == "5":  # delete
            df = delete_record(df)
        elif choice == "6":  # quiz
            play_quiz(df)
        elif choice == "7":  # report
            analysis.summary_report(df)
        elif choice == "8":  # numpy
            analysis.numpy_analysis(df)
        elif choice == "9":  # pandas
            analysis.pandas_analysis(df)
        elif choice == "0":  # exit
            print("Thanks for using Quiz Generator!")  # bye
            break  # loop khatam
        else:  # galat choice
            print("Galat choice! 0 se 9 ke beech daalo.")  # message


if __name__ == "__main__":  # file direct run hone par
    main()  # program start8