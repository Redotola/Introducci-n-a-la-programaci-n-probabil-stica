"GIGO: Garbage In, Garbage Out"
"Si entran datos basura, basura saldra"

def calc_bayes(prior_A, prob_B_dado_A, pro_B):
    return (prior_A * prob_B_dado_A) / pro_B

if __name__ == '__main__':
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer
    
    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)
    
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    print(f"La probabilidad de tener cancer dado que se presentan sintomas es de: {prob_cancer_dado_sintoma}")

