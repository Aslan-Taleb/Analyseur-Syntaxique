# PARTIE GRAMMAIRE

# Tableau terminaux
tabTerminaux = ["main()", "int", "float", "id", "if", "else",
                "=", "<", ">", "{", "}", "$", '']
"""
tabTerminaux[0] = "main()"
tabTerminaux[1] = "int"
tabTerminaux[2] = "float"
tabTerminaux[3] = "id"
tabTerminaux[4] = "if"
tabTerminaux[5] = "else"
tabTerminaux[6] = "="
tabTerminaux[7] = "<"
tabTerminaux[8] = ">"
tabTerminaux[9] = "{"
tabTerminaux[10] = "}"
tabTerminaux[11] = "$"
tabTerminaux[12] = ''
"""

#Tableau nonTerminaux
tabNonTerminaux = ["Programme", "liste_declarations", "liste_instructions", "une_declaration", "une_instruction", "affectation", "type",
                                "test", "condition", "operateur"]
"""
tabNonTerminaux[0] = "<Programme>"
tabNonTerminaux[1] = "<liste_declarations>"
tabNonTerminaux[2] = "<liste_instructions>"
tabNonTerminaux[3] = "<une_declaration>"
tabNonTerminaux[4] = "<une_instruction>"
tabNonTerminaux[5] = "<affectation>"
tabNonTerminaux[6] = "<type>"
tabNonTerminaux[7] = "<test>"
tabNonTerminaux[8] = "<condition>"
tabNonTerminaux[9] = "<operateur>"

"""