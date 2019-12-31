# Automated-Sequent-Prover

This project was created as a solution to a question in one my assignments from COMP4418 - Knowledge Representation and Reasoning, a course I took at the University of New South Wales during my time studying abroad in Sydney, Australia in 2019.

## Excerpt of Original Problem Statement
### Background
In 1958 the logician Hao Wang implemented one of the first automated theorem provers. He succeeded in writing several programs capable of automatically proving a majority of theorems from the first five chapters of Whitehead and Russell’s Principia Mathematica (in fact, his program managed to prove over 200 of these theorems “within about 37 minutes, and 12/13 of the time is used for read-in and print-out”). This was an impressive achievement at the time; previous attempts had only succeeded in proving a handful of the theorems in Principia Mathematica.

Wang’s idea is based around the notion of a sequent (this idea had been introduced years earlier by Gentzen) and the manipulation of sequents. A sequent is essentially a list of formulae on either side of a sequent (or provability) symbol ⊢. The sequent π ⊢ ρ, where π and ρ are strings (i.e., lists) of formulae, can be read as “the formulae in the string ρ follow from the formulae in the string π” (or, equivalently, “the formulae in string π prove the formulae in string ρ”).

To prove whether a given sequent is true all you need to do is start from some basic sequents and successively apply a series of rules that transform sequents until you end up with the sequent you desire. This process is detailed below.

Additionally, determining whether a formula φ is a theorem, is equivalent to determining whether the sequent ∅ ⊢ φ is true (e.g., ⊢ ¬φ ∨ φ).

### Rules
P1 Initial Rule: If λ, ζ are strings of atomic formulae, then λ ⊢ ζ is a theorem if some atomic formula occurs on both side of the sequent ⊢.

In the following ten rules λ and ζ are always strings (possibly empty) of formulae. 

P2a Rule ⊢¬: If φ, ζ ⊢ λ, ρ, then ζ  ⊢λ, ¬φ, ρ

P2b Rule ¬⊢: If λ, ρ ⊢ π, φ, then λ, ¬φ, ρ ⊢ π

P3a Rule ⊢∧: If ζ ⊢ λ, φ, ρ and ζ ⊢ λ, ψ, ρ, then ζ  ⊢λ, φ∧ψ, ρ

P3b Rule ∧⊢: If λ, φ, ψ, ρ ⊢ π, then λ, φ∧ψ, ρ ⊢ π

P4a Rule ⊢∨: If ζ ⊢ λ, φ, ψ, ρ, then ζ ⊢ λ, φ∨ψ, ρ

P4b Rule ∨⊢: If λ, φ, ρ ⊢ π and λ, ψ, ρ ⊢ π, then λ, φ∨ψ, ρ ⊢ π

P5a Rule ⊢→: If ζ, φ ⊢ λ, ψ, ρ, then ζ ⊢ λ, φ→ψ, ρ

P5b Rule →⊢: If λ, ψ,  ρ ⊢ π and λ, ρ ⊢ π, φ, then λ, φ→ψ, ρ ⊢ π

P6a Rule ⊢↔: If φ, ζ ⊢ λ, ψ, ρ and ψ, ζ ⊢ λ, φ, ρ, then ζ ⊢ λ, φ↔ψ, ρ 

P6b Rule ↔⊢: If φ, ψ, λ, ρ ⊢ π and λ, ρ ⊢ π, φ, ψ, then λ, φ↔ψ, ρ ⊢ π


## Input
The input consists of a single sequent on the command line. Sequents are written as:

[List of Formulae] seq [List of Formulae]. 

To construct formulae, atoms can be any string of characters (without space) and connectives as follows:

• ¬: neg 

• ∧: and 

• ∨: or

• →: imp 

• ↔: iff

So, for example, the sequent p→q, ¬r→¬q ⊢ p→r would be written as: [p imp q, (neg r) imp (neg q)] seq [p imp r]

The program is called seqprove and run as follows: 
```
./seqprove ’Sequent’
```
For example
```
  ./seqprove ’[p imp q, (neg r) imp (neg q)] seq [p imp r]’
```
## Output
The output consists of the proof for the given sequent if it is determined to be true, i.e. it is a theorem. For example, the sequent above would return the proof:
```
-----------------------------------------------------
Input: (p → q), (¬r → ¬q) ⊢ (p → r)
-----------------------------------------------------
1.   r, p ⊢ p, r                  Rule 1                            
2.   p ⊢ ¬r, p, r                 Rule 2a applied to line 1         
3.   p ⊢ q, p, r                  Rule 1                            
4.   p, ¬q ⊢ p, r                 Rule 2b applied to line 3         
5.   p, (¬r → ¬q) ⊢ p, r          Rule 5b applied to lines 2 and 4  
6.   r, p, q ⊢ r                  Rule 1                            
7.   p, q ⊢ ¬r, r                 Rule 2a applied to line 6         
8.   p, q ⊢ q, r                  Rule 1                            
9.   p, q, ¬q ⊢ r                 Rule 2b applied to line 8         
10.  p, q, (¬r → ¬q) ⊢ r          Rule 5b applied to lines 7 and 9  
11.  p, (p → q), (¬r → ¬q) ⊢ r    Rule 5b applied to lines 5 and 10 
12.  (p → q), (¬r → ¬q) ⊢ (p → r) Rule 5a applied to line 11        
QED
-----------------------------------------------------
```
