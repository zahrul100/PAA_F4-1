from daftarkota import daftarkota
from greedy import Greedy
def main():
	#List Kota
	kota = set(['Cilegon', 'Tangerang', 'Jakarta', 'Bogor',
		'Cikampek', 'Bekasi', 'Bandung', 'Cirebon', 'Cimahi', 'Cianjur', 'Garut', 'Sumedang', 'Subang', 'Tasikmalaya',	
		'Purwokerto', 'Magelang', 'Semarang', 'Jogja', 'Surabaya',
		'Malang'])

	#adjacency list city in Java
	jarak = {		
        'Cilegon' : {'Tanggerang' : 84},
		'Tanggerang' : {'Jakarta' : 35, 'Cilegon' : 84},
		'Jakarta' : {'Bogor' : 54, 'Cikampek' : 76, 'Bekasi' : 50, 'Tanggerang' : 35},
		'Bekasi' : {'Cikampek' : 41, 'Jakarta' : 50},
		'Cikampek' : {'Bandung' : 80, 'Cirebon' : 146, 'Jakarta' : 76, 'Bekasi' : 41},
		'Bogor' : {'Bandung' : 182, 'Jakarta' : 54},
		'Bandung' : {'Tasikmalaya' : 124, 'Cimahi' : 14, 'Cianjur' : 67, 'Garut' : 71, 'Sumedang' : 76, 'Subang': 54, 'Cikampek' : 80, 'Bogor' : 182},
			
	}

	finish = ' '
	daftarkota(finish,kota)
	start = input('Kota Anda Sekarang : ').strip()
	start = start.lower()
	start = ''.join(start[0].upper() + start[1:])
	if start not in kota:
		print('\n Kota Yang Anda Masukkan Salah')
		
    
	finish = input('Kota Tujuan Anda : ')
	path = Greedy(jarak, start, finish)
	print('Kota Asal = ',start)
	if (path):
		print('Urutan Kota Berdasar Algoritma Greedy : ', end='')
		for i in path:
			print(i, end='>')

	else:
		print('Tidak Ditemukan Jalan')
	

if __name__ == '__main__':
	main()
