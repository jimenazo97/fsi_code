# Search methods
#buasss chiquita bomba primo
#vamo s añaidir cosas
import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
#leañadomaslineasporlaprueba1
cr = search.GPSProblem('C', 'R'
                       , search.romania)
ve=search.GPSProblem('V', 'E'
                       , search.romania)
sn=search.GPSProblem('S', 'N'
                       , search.romania)
df=search.GPSProblem('D', 'F'
                       , search.romania)
#archivo=open("/Users/andresjimenez/Desktop/IA/PycharmProjects/code/salida.txt","a")
#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

print("De A a B",search.rya_first_graph_search(ab).path())
print("De A a B con Subestimación",search.rya_sub_first_graph_search(ab).path())

print("De C a R",search.rya_first_graph_search(cr).path())
print("De C a R con Subestimación",search.rya_sub_first_graph_search(cr).path())

print("De V a E",search.rya_first_graph_search(ve).path())
print("De V a E con Subestimación",search.rya_sub_first_graph_search(ve).path())

print("De S a N",search.rya_first_graph_search(sn).path())
print("De S a N con Subestimación",search.rya_sub_first_graph_search(sn).path())
print("De D a F",search.rya_first_graph_search(df).path())
print("De D a F con Subestimación",search.rya_sub_first_graph_search(df).path())

#archivo.write("De A a B" + str(search.rya_first_graph_search(ab).path()) + "\n" +
#"De A a B con Subestimación" + str(search.rya_sub_first_graph_search(ab).path()) + "\n" +

#("De C a R" + str(search.rya_first_graph_search(cr).path())) + "\n" +
#("De C a R con Subestimación" + str(search.rya_sub_first_graph_search(cr).path())) + "\n" +

#("De V a E" + str(search.rya_first_graph_search(ve).path())) + "\n" +
#("De V a E con Subestimación" + str(search.rya_sub_first_graph_search(ve).path())) + "\n" +

#("De S a N" + str(search.rya_first_graph_search(sn).path())) + "\n" +
#("De S a N con Subestimación" + str(search.rya_sub_first_graph_search(sn).path())) + "\n" +

#("De D a F"+ str(search.rya_first_graph_search(df).path())) + "\n" +
#("De D a F con Subestimación"+ str(search.rya_sub_first_graph_search(df).path())))

#archivo.close()
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
