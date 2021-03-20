def vote(voters,politicians,voter,politician):
    voters[voter] = politician
    if politician in politicians:
        politicians[politician]+=1
    else:
        politicians[politician] = 1
    return voters,politicians

def voted_for(voters,voter):
    return f"{voter} voted for {voters.get(voter,None)}"

def votes(politicians,politician):
    return f"{politician} received {politicians.get(politician, None)} votes"

voters,politicians = vote({},{},'Joe','Trump')
print(voted_for(voters,'Joe'))
print(votes(politicians,'Trump'))




# def main():
#
# if __name__ == '__main__':
#     main()
