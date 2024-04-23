import pandas as pd
import math

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# inputs: numerator and denominator.
# -(numer/denom) * log_2(numer/denom)
def log_fraction_calc(numer: int, denom: int) -> float:
    if numer == 0:
        return 0
    return -1 * (numer/denom) * math.log2(numer/denom)

def conditional_entropy_calculation(condition_row_name: str, df) -> float:
    count_all_rows = len(df)

    count_true_cond1 = (df[condition_row_name] == True).sum()

    count_true_c1_A = ((df[condition_row_name] == True) & (df['Action'] == 'A')).sum()
    count_true_c1_B = ((df[condition_row_name] == True) & (df['Action'] == 'B')).sum()
    count_true_c1_C = ((df[condition_row_name] == True) & (df['Action'] == 'C')).sum()
    count_true_c1_FACE = ((df[condition_row_name] == True) & (df['Action'] == 'FACE')).sum()

    cond_entr_true_portion = (count_true_cond1/count_all_rows) * (log_fraction_calc(count_true_c1_A, count_true_cond1) + log_fraction_calc(count_true_c1_B, count_true_cond1) + log_fraction_calc(count_true_c1_C, count_true_cond1) + log_fraction_calc(count_true_c1_FACE, count_true_cond1))

    count_false_cond1 = (df[condition_row_name] == False).sum()

    count_false_c1_A = ((df[condition_row_name] == False) & (df['Action'] == 'A')).sum()
    count_false_c1_B = ((df[condition_row_name] == False) & (df['Action'] == 'B')).sum()
    count_false_c1_C = ((df[condition_row_name] == False) & (df['Action'] == 'C')).sum()
    count_false_c1_FACE = ((df[condition_row_name] == False) & (df['Action'] == 'FACE')).sum()

    cond_entr_false_portion = (count_false_cond1/count_all_rows) * (log_fraction_calc(count_false_c1_A, count_false_cond1) + log_fraction_calc(count_false_c1_B, count_false_cond1) + log_fraction_calc(count_false_c1_C, count_false_cond1) + log_fraction_calc(count_false_c1_FACE, count_false_cond1))

    conditional_entropy = cond_entr_true_portion + cond_entr_false_portion

    return conditional_entropy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Path to the CSV file
    file_path = 'input/log_record_1.csv'

    # Reading the CSV data into DataFrame without parsing dates
    df = pd.read_csv(file_path, header=None, sep=',')
    df.columns = ['Date', 'Level', 'Cond_1', 'Cond_2', 'Cond_3', 'Cond_4', 'Cond_5', 'Action']

    count_all_rows = len(df)

    count_true_cond1 = (df['Cond_1'] == True).sum()

    count_true_c1_A = ((df['Cond_1'] == True) & (df['Action'] == 'A')).sum()
    count_true_c1_B = ((df['Cond_1'] == True) & (df['Action'] == 'B')).sum()
    count_true_c1_C = ((df['Cond_1'] == True) & (df['Action'] == 'C')).sum()
    count_true_c1_FACE = ((df['Cond_1'] == True) & (df['Action'] == 'FACE')).sum()

    cond_entr_true_portion = (count_true_cond1/count_all_rows) * (log_fraction_calc(count_true_c1_A, count_true_cond1) + log_fraction_calc(count_true_c1_B, count_true_cond1) + log_fraction_calc(count_true_c1_C, count_true_cond1) + log_fraction_calc(count_true_c1_FACE, count_true_cond1))

    count_false_cond1 = (df['Cond_1'] == False).sum()

    count_false_c1_A = ((df['Cond_1'] == False) & (df['Action'] == 'A')).sum()
    count_false_c1_B = ((df['Cond_1'] == False) & (df['Action'] == 'B')).sum()
    count_false_c1_C = ((df['Cond_1'] == False) & (df['Action'] == 'C')).sum()
    count_false_c1_FACE = ((df['Cond_1'] == False) & (df['Action'] == 'FACE')).sum()

    cond_entr_false_portion = (count_false_cond1/count_all_rows) * (log_fraction_calc(count_false_c1_A, count_false_cond1) + log_fraction_calc(count_false_c1_B, count_false_cond1) + log_fraction_calc(count_false_c1_C, count_false_cond1) + log_fraction_calc(count_false_c1_FACE, count_false_cond1))

    conditional_entropy = cond_entr_true_portion + cond_entr_false_portion

    cond_entr_1 = conditional_entropy_calculation('Cond_1', df)
    cond_entr_2 = conditional_entropy_calculation('Cond_2', df)
    cond_entr_3 = conditional_entropy_calculation('Cond_3', df)
    cond_entr_4 = conditional_entropy_calculation('Cond_4', df)
    cond_entr_5 = conditional_entropy_calculation('Cond_5', df)

    print("CONDITION 1: ... ", cond_entr_1)
    print("CONDITION 2: ... ", cond_entr_2)
    print("CONDITION 3: ... ", cond_entr_3)
    print("CONDITION 4: ... ", cond_entr_4)
    print("CONDITION 5: ... ", cond_entr_5)

    # 1.0902, 0.7974, 1.5322, 1.5727, 1.6384
    # MINIMIZE conditional entropy
    # Minimal entropy condition: Condition #2

    df_cond2_true = df[df['Cond_2'] == True]
    df_cond2_false = df[df['Cond_2'] == False]

    # Looking at if Cond2 is true.
    cond_entr_1_2t = conditional_entropy_calculation('Cond_1', df_cond2_true)
    cond_entr_3_2t = conditional_entropy_calculation('Cond_3', df_cond2_true)
    cond_entr_4_2t = conditional_entropy_calculation('Cond_4', df_cond2_true)
    cond_entr_5_2t = conditional_entropy_calculation('Cond_5', df_cond2_true)
    # All are 0, therefore no more child conditional nodes below if Condition 2 is true.

    # Looking at if Cond2 is false.
    cond_entr_1_2f = conditional_entropy_calculation('Cond_1', df_cond2_false)
    cond_entr_3_2f = conditional_entropy_calculation('Cond_3', df_cond2_false)
    cond_entr_4_2f = conditional_entropy_calculation('Cond_4', df_cond2_false)
    cond_entr_5_2f = conditional_entropy_calculation('Cond_5', df_cond2_false)
    # Winner is Cond1.

    # If cond2 is false, then cond1. If cond2 is true, no more conditional nodes.

    # Finding the next learning decision tree nodes after Condition 2 and Condition 1:
    df_cond1_true = df[(df['Cond_2'] == False) & (df['Cond_1'] == True)]
    df_cond1_false = df[(df['Cond_2'] == False) & (df['Cond_1'] == False)]

    cond_entr_3_1t = conditional_entropy_calculation('Cond_3', df_cond1_true)
    cond_entr_4_1t = conditional_entropy_calculation('Cond_4', df_cond1_true)
    cond_entr_5_1t = conditional_entropy_calculation('Cond_5', df_cond1_true)
    # Condition #3 is the winner, if Condition 1 is true after Condition 2 is false.

    cond_entr_3_1f = conditional_entropy_calculation('Cond_3', df_cond1_false)
    cond_entr_4_1f = conditional_entropy_calculation('Cond_4', df_cond1_false)
    cond_entr_5_1f = conditional_entropy_calculation('Cond_5', df_cond1_false)
    # Condition #4 is the winner, if Condition 1 is false after Condition 2 is false.

    # Investigating the decision tree path: 2, 1, 3:
    df_cond3_true = df[(df['Cond_2'] == False) & (df['Cond_1'] == True) & (df['Cond_3'] == True)]
    df_cond3_false = df[(df['Cond_2'] == False) & (df['Cond_1'] == True) & (df['Cond_3'] == False)]

    cond_entr_4_3t = conditional_entropy_calculation('Cond_4', df_cond3_true)
    cond_entr_5_3t = conditional_entropy_calculation('Cond_5', df_cond3_true)
    # Condition #4 is winner.

    cond_entr_4_3f = conditional_entropy_calculation('Cond_4', df_cond3_false)
    cond_entr_5_3f = conditional_entropy_calculation('Cond_5', df_cond3_false)
    # Condition #4 is winner.

    # Investigating the decision tree path: 2, 1, 4:
    df_cond4_true = df[(df['Cond_2'] == False) & (df['Cond_1'] == False) & (df['Cond_4'] == True)]
    df_cond4_false = df[(df['Cond_2'] == False) & (df['Cond_1'] == False) & (df['Cond_4'] == False)]

    cond_entr_3_4t = conditional_entropy_calculation('Cond_3', df_cond4_true)
    cond_entr_5_4t = conditional_entropy_calculation('Cond_5', df_cond4_false)
    # 5 is winner.

    cond_entr_3_4f = conditional_entropy_calculation('Cond_3', df_cond4_true)
    cond_entr_5_4f = conditional_entropy_calculation('Cond_5', df_cond4_false)
    # 5 is winner.

    # Show the DataFrame
    print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/










