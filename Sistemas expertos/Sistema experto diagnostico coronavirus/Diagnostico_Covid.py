from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		
		print("")
		print("-----------------------------------------------------------------------------")
		print("la enfermedad mas problable que tiene es %s\n" %(id_disease))
		print("")
		print("-----------------------------------------------------------------------------")
		print("A continuacion se proporcionara una breve descripcion de las enfermedad  :\n") 
		print(disease_details+"\n")
		print("")
		print("-----------------------------------------------------------------------------")
		print("los medicamentos y tratamientos son los siguientes: \n")
		print(treatments+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Vomito, Dolor_de_garganta, Flema,Dificultad_para_respirar ,Diarrea,Malestar_en_la_garganta):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hola soy el doctor Yulian, el objetivo de este Sistema Experto .")
		print("Es poder diagnosticar si presenta alguna de las siguientes enfermedades Coronavirus,Gripe o Resfriado")
		print("si presenta alguno de los sintomas por favor responder las siguientes preguntas ")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(Fiebre=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(Fiebre=input("Fiebre: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Tos=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(Tos=input("Tos: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Moco=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(Moco=input("Moco: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Congestion_nasal=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(Congestion_nasal=input("Congestion nasal: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Estornudos=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(Estornudos=input("Estornudos: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Dolor_de_garganta=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(Dolor_de_garganta=input("Dolor de garganta: ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(Malestar_en_la_garganta=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(Malestar_en_la_garganta=input("Malestar en la garganta: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Dificultad_para_respirar=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(Dificultad_para_respirar=input("Dificultad para respirar: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Flema=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(Flema=input("Flema: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Vomito=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(Vomito=input("Vomito: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Diarrea=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(Diarrea=input("Diarrea: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Debilidad=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(Debilidad=input("Debilidad: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Dolor_de_huesos=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(Dolor_de_huesos=input("Dolor de huesos: ")))
		
	
	@Rule(Fact(action='find_disease'), NOT(Fact(pulmon=W())),salience = 1)
	def symptom_13(self):
		self.declare(Fact(Dolor_de_huesos=input("Pulmon con mancha: ")))
		
		
		
	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="si"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="si"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_0(self):
		self.declare(Fact(disease="Fiebre"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="si"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_1(self):
		self.declare(Fact(disease="Tos"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="si"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="si"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_2(self):
		self.declare(Fact(disease="Moco"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="si"),Fact(Congestion_nasal="si"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="si"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_3(self):
		self.declare(Fact(disease="Congestion_nasal"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="si"),Fact(Congestion_nasal="si"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="si"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_4(self):
		self.declare(Fact(disease="Estornudos"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="si"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="si"),Fact(Estornudos="no"),Fact(Vomito="si"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="si"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_5(self):
		self.declare(Fact(disease="Dolor de garganta"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="si"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_6(self):
		self.declare(Fact(disease="Malestar en la garganta"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="si"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_7(self):
		self.declare(Fact(disease="Dificultad para respirar"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="si"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="si"),Fact(pulmon="no"))
	def disease_8(self):
		self.declare(Fact(disease="Flema"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="si"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="si"),Fact(pulmon="no"))
	def disease_9(self):
		self.declare(Fact(disease="Vomito"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="si"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_10(self):
		self.declare(Fact(disease="Diarrea"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="si"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="no"),Fact(Diarrea="si"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="si"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_11(self):
		self.declare(Fact(disease="Debilidad"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="si"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="si"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_12(self):
		self.declare(Fact(disease="Dolor de huesos"))
		
	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="no"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="si"),Fact(Vomito="no"),Fact(Dolor_de_garganta="no"),Fact(Flema="no"),Fact(Dificultad_para_respirar="si"),Fact(Diarrea="no"),Fact(Malestar_en_la_garganta="no"),Fact(Debilidad="no"),Fact(Dolor_de_huesos="no"),Fact(pulmon="no"))
	def disease_13(self):
		self.declare(Fact(disease="Pulmon con mancha"))
		
		

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("-----------------------------------------------------------------------------")
		print("la enfermedad mas problable que tiene es %s\n" %(id_disease))
		print("")
		print("-----------------------------------------------------------------------------")
		print("A continuacion se proporcionara una breve descripcion de las enfermedad :\n")
		print("")
		print(disease_details+"\n")
		print("")
		print("-----------------------------------------------------------------------------")
		print("los medicamentos y tratamientos son los siguientes: \n")
		print("")
		print(treatments+"\n")
		print("")

	@Rule(Fact(action='find_disease'),
		  Fact(Fiebre=MATCH.Fiebre),
		  Fact(Tos=MATCH.Tos),
		  Fact(Moco=MATCH.Moco),
		  Fact(Congestion_nasal=MATCH.Congestion_nasal),
		  Fact(Estornudos=MATCH.Estornudos),
		  Fact(Vomito=MATCH.Vomito),
		  Fact(Dolor_de_garganta=MATCH.Dolor_de_garganta),
		  Fact(Dificultad_para_respirar=MATCH.Dificultad_para_respirar),
		  Fact(Flema=MATCH.Flema),
		  Fact(Diarrea=MATCH.Diarrea),
		  Fact(Malestar_en_la_garganta=MATCH.Malestar_en_la_garganta),
		  Fact(Debilidad=MATCH.Debilidad),
		  Fact(Dolor_de_huesos=MATCH.Dolor_de_huesos),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Vomito, Dolor_de_garganta, Flema,Dificultad_para_respirar ,Diarrea ,Malestar_en_la_garganta ,Debilidad ,Dolor_de_huesos):
		print("-----------------------------------------------------------------------------")
		print("\nle gustaria diagnosticar algun otro sintoma?")
		lis = [Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Vomito, Dolor_de_garganta, Flema,Dificultad_para_respirar ,Diarrea ,Malestar_en_la_garganta ,Debilidad ,Dolor_de_huesos]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "si"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("-----------------------------------------------------------------------------")
		print("le gustaria diagnosticar algun otro sintoma?")
		if input() == "no":
			exit()
		#print(engine.facts)