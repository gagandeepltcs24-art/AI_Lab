knowledge_base = [
    [
        ("Human", "x", True),
        ("Mortal", "x", False)
    ],
    [
        ("Human", "Socrates", False)
    ]
]

query_negation = [
    ("Mortal", "Socrates", True)
]

knowledge_base.append(query_negation)


def is_variable(term):
    return term.islower()


def unify(term1, term2):
    if term1 == term2:
        return {}

    if is_variable(term1):
        return {term1: term2}

    if is_variable(term2):
        return {term2: term1}

    return None


def apply_substitution(literal, substitution):
    predicate, argument, negation = literal

    while argument in substitution:
        argument = substitution[argument]

    return (predicate, argument, negation)


def resolve(clause1, clause2):

    for literal1 in clause1:
        for literal2 in clause2:

            if (literal1[0] == literal2[0] and
                literal1[2] != literal2[2]):

                substitution = unify(
                    literal1[1],
                    literal2[1]
                )

                if substitution is not None:

                    new_clause = []

                    for literal in clause1:
                        if literal != literal1:
                            new_clause.append(
                                apply_substitution(
                                    literal, substitution
                                )
                            )

                    for literal in clause2:
                        if literal != literal2:
                            new_clause.append(
                                apply_substitution(
                                    literal, substitution
                                )
                            )

                    return new_clause

    return None


print("Knowledge Base:")
for clause in knowledge_base:
    print(clause)

print("\nResolution Steps:")

clause1 = knowledge_base[0]
clause2 = knowledge_base[1]

result1 = resolve(clause1, clause2)

print("Step 1:", result1)

result2 = resolve(result1, knowledge_base[2])

print("Step 2:", result2)

if result2 == []:
    print("\nQuery is proved using Resolution!")
else:
    print("\nQuery could not be proved.")



Output:

Knowledge Base:
[('Human', 'x', True), ('Mortal', 'x', False)]
[('Human', 'Socrates', False)]
[('Mortal', 'Socrates', True)]

Resolution Steps:
Step 1: [('Mortal', 'Socrates', False)]
Step 2: []

Query is proved using Resolution!
