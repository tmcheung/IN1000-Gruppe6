fn_peter = "Peter.txt"
fn_paul = "Paul.txt"
prosedyre("Peter",fn_peter)
prosedyre("Paul", fn_paul)

def prosedyre(navn, filnavn):
	tot_navn=0

	for line in open(filnavn):
		utgift_navn = int(line)
		tot_navn += utgift_navn
		print(navn + " har brukt: ", tot_navn)
	
