import matplotlib.pyplot as plt
import scipy.stats as stats
import math

def benford_first_digit(df, col):
    """
    Statistically analyze consistency with Benford's law (first digit)
    """

    #Convert the column values to positive integers unequal to 0
    df[col] = df[col].abs().astype(int)
    df = df[df[col] != 0]
    obs = df[col]

    #Create a list of the first two digits of the amounts
    def first_digit(num):
        return int(str(num)[0])
    obs = [first_digit(n) for n in obs]

    #Create a dictionary with the observed frequencies (counts)
    dict1 = {x: 0 for x in range(1, 10)}
    for num in obs:
        dict1[num] += 1

    #Calculate the number of observations and assign it to a variable
    n = len(obs)

    #Create a dictionary with the expected frequencies    
    dict2 = {x: round(n * math.log10(1+(1/x)), 0) for x in range(1, 10)}

    #Convert the dictionaries to lists
    obs = list(dict1.values())
    exp = list(dict2.values())
    x = list(dict2.keys())

    #Print the observed and expected frequencies
    print(obs)
    print(exp)

    #Normalize the data such that the observed and expected frequencies have the same sum
    if sum(obs) != sum(exp):
        exp = [i * (sum(obs)/sum(exp)) for i in exp]

    #Test for differences using the one-sample Chi-Square test
    chi_sq = stats.chisquare(obs, f_exp=exp)
    chi_sq_stat = (chi_sq[0].round(3))
    chi_sq_pvalue = (("<0.01" if chi_sq[1] < 0.01 else chi_sq[1].round(3)))
    print(f"One-sample Chi-Square test statistic = {chi_sq_stat}; p-value = {chi_sq_pvalue}")

    #Graphically analyze consistency with Benford's law (first digit)
    plt.plot(x, obs, c='r', marker= '.')
    plt.plot(x, exp, c='b', marker= '.')
    plt.xlabel('First digit')
    plt.ylabel('Frequency')
    plt.title("Observed vs. expected frequencies (Benford's law)");


def benford_first_two_digits(df, col):
    """
    Statistically analyze consistency with Benford's law (first two digits)
    """

    #Convert the column values to positive integers unequal to 0 and larger than 9
    df[col] = df[col].abs().astype(int)
    df = df[df[col] != 0]
    df = df[df[col] > 9]
    obs = df[col]

    #Create a list of the first two digits of the amounts
    def first_two_digits(num):
        return int(str(num)[:2])
    obs = [first_two_digits(n) for n in obs]

    #Create a dictionary with the observed frequencies (counts)
    dict1 = {x: 0 for x in range(10, 100)}
    for num in obs:
        dict1[num] += 1

    #Calculate the number of observations and assign it to a variable
    n = len(obs)

    #Create a dictionary with the expected frequencies
    dict2 = {x: round(n * math.log10(1+(1/x)), 0) for x in range(10, 100)}

    #Convert the dictionaries to lists
    obs = list(dict1.values())
    exp = list(dict2.values())
    x = list(dict2.keys())

    #Print the observed and expected frequencies
    print(obs)
    print(exp)

    #Normalize the data such that the observed and expected frequencies have the same sum
    if sum(obs) != sum(exp):
        exp = [i * (sum(obs)/sum(exp)) for i in exp]
    
    #Test for differences using the one-sample Chi-Square test
    chi_sq = stats.chisquare(obs, f_exp=exp)
    chi_sq_stat = (chi_sq[0].round(3))
    chi_sq_pvalue = (("<0.01" if chi_sq[1] < 0.01 else chi_sq[1].round(3)))
    print(f"One-sample Chi-Square test statistic = {chi_sq_stat}; p-value = {chi_sq_pvalue}")

    #Graphically analyze consistency with Benford's law (first two digits)
    plt.plot(x, obs, c='r', marker= '.')
    plt.plot(x, exp, c='b', marker= '.')
    plt.xlabel('First two digits')
    plt.ylabel('Frequency')
    plt.title("Observed vs. expected frequencies (Benford's law)");


def uniform_last_digit(df, col):
    """
    Statistically analyze consistency with uniform distribution (last digit)
    """

    #Convert the column values to positive integers unequal to 0
    df[col] = df[col].abs().astype(int)
    df = df[df[col] != 0]
    obs = df[col]
    
    #Create a list of the last digit of the amounts
    obs = [num % 10 for num in obs]

    #Create a dictionary with the observed frequencies (counts)
    dict1 = {x: 0 for x in range(0, 10)}
    for num in obs:
        dict1[num] += 1

    #Calculate the number of observations and assign it to a variable
    n = len(obs)

    #Create a dictionary with the expected frequencies
    dict2 = {x: round(n * 0.1, 1) for x in range(0, 10)}

    #Convert the dictionaries to lists
    obs = list(dict1.values())
    exp = list(dict2.values())
    x = list(dict1.keys())

    #Print the observed and expected frequencies
    print(obs)
    print(exp)

    #Normalize the data such that the observed and expected frequencies have the same sum
    if sum(obs) != sum(exp):
        exp = [i * (sum(obs)/sum(exp)) for i in exp]

    #Test for differences using the one-sample Chi-Square test
    chi_sq = stats.chisquare(obs, f_exp=exp)
    chi_sq_stat = (chi_sq[0].round(3))
    chi_sq_pvalue = (("<0.01" if chi_sq[1] < 0.01 else chi_sq[1].round(3)))
    print(f"One-sample Chi-Square test statistic = {chi_sq_stat}; p-value = {chi_sq_pvalue}")

    #Graphically analyze consistency with uniform distribution (last digit)
    plt.plot(x, obs, c='r', marker= '.')
    plt.plot(x, exp, c='b', marker= '.')
    plt.xlabel('Last digit')
    plt.ylabel('Frequency')
    plt.title("Observed vs. expected frequencies (uniform distribution)");