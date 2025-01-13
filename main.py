import string

n_docs = int(input())

docs_tokens = []

for n in range(n_docs): 
    doc = input().strip().lower()
    doc = doc.translate(str.maketrans('', '', string.punctuation))
    doc_tokens = doc.split()
    docs_tokens.append(doc_tokens)

q = input()
q_tokens = q.split()

lambd = 0.5

L_d = [len(doc_tokens) for doc_tokens in docs_tokens]

c = [token for doc_tokens in docs_tokens for token in doc_tokens]
L_c = len(c)

token_counts = [[doc.count(token) for token in q_tokens] for doc in docs_tokens]
P_t_Md = [[count / len for count in sublist] for sublist, len in zip(token_counts, L_d)]

token_counts_c = [c.count(token) for token in q_tokens]
P_t_Mc = [count/L_c for count in token_counts_c]

P_t_d = [[lambd * count + (1-lambd) * M_j for count, M_j in zip(counts, P_t_Mc)] for counts in P_t_Md]

P_t_d_multiplied = [eval('*'.join(map(str, P_t_dj))) for P_t_dj in P_t_d]

result = sorted(range(len(P_t_d_multiplied)), key=lambda i: P_t_d_multiplied[i], reverse=True)

print(result)