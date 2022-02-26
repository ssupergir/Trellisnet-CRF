# -*- coding: utf-8 -*-
from py2neo import Graph,Node,Relationship,NodeMatcher
#版本说明：Py2neo v4
class Neo4j_Handle():
	graph = None
	matcher = None
	def __init__(self):
		print("Neo4j Init ...")

	def connectDB(self):
		self.graph = Graph("bolt: // localhost:7687", username="oceanexpert", password="wjj198947")
		self.matcher = NodeMatcher(self.graph)

	#实体查询，用于命名实体识别：品牌+车系+车型
	def matchEntityItem(self,value):
		answer = self.graph.run("MATCH (entity1:`专家`) WHERE entity1.name = \"" + value + "\" RETURN entity1").data()
		# print("MATCH (entity1:`专家`) WHERE entity1.name = \"" + value + "\" RETURN entity1")
		return answer

	#实体查询
	def getEntityRelationbyEntity(self,value):
		#查询实体：不考虑实体类型，只考虑关系方向
		answer = self.graph.run("MATCH (entity1) - [rel:belong|good_field|location|work] -> (entity2)  WHERE entity1.name = \"" + value + "\" RETURN rel,entity2,TYPE(rel) limit 200").data()
		if(len(answer) == 0):
			#查询实体：不考虑关系方向
			answer = self.graph.run("MATCH (entity1) - [rel:belong|good_field|location|work] - (entity2)  WHERE entity1.name = \"" + value + " \" RETURN rel,entity2,TYPE(rel) limit 200").data()
		return answer
	#实体查询
	def getPaperEntityRelationbyEntity(self,value):
		#查询实体：不考虑实体类型，只考虑关系方向
		answer = self.graph.run("MATCH (entity1) - [rel:paper] -> (entity2)  WHERE entity1.name = \"" + value + "\" RETURN rel,entity2,TYPE(rel) limit 200").data()
		if(len(answer) == 0):
			#查询实体：不考虑关系方向
			answer = self.graph.run("MATCH (entity1) - [rel:paper] - (entity2)  WHERE entity1.name = \"" + value + " \" RETURN rel,entity2,TYPE(rel) limit 200").data()
		return answer

	#实体查询
	def getCooEntityRelationbyEntity(self,value):
		#查询实体：不考虑实体类型，只考虑关系方向
		answer = self.graph.run("MATCH (entity1) - [rel:cooperation] -> (entity2)  WHERE entity1.name = \"" + value + "\" RETURN rel,entity2,TYPE(rel) limit 200").data()
		if(len(answer) == 0):
			#查询实体：不考虑关系方向
			answer = self.graph.run("MATCH (entity1) - [rel:cooperation] - (entity2)  WHERE entity1.name = \"" + value + " \" RETURN rel,entity2,TYPE(rel) limit 200").data()
		return answer
	#关系查询:实体1
	def findRelationByEntity1(self,entity1):
		#基于品牌查询
		answer = self.graph.run("MATCH (n1:`专家` {name:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,TYPE(rel),n2" ).data()
		return answer

	#关系查询：实体2
	def findRelationByEntity2(self,entity1):
		#基于品牌
		answer = self.graph.run("MATCH (n1)<- [rel] - (n2 {name:\""+entity1+"\"}) RETURN n1,rel,TYPE(rel),n2" ).data()
		return answer

	#关系查询：实体1+关系
	def findOtherEntities(self,entity,relation):
		answer = self.graph.run("MATCH (n1:`专家` {name:\"" + entity + "\"})- [rel:"+relation+"] -> (n2) RETURN n1,rel,TYPE(rel),n2" ).data()
		print("MATCH (n1:`专家` {name:\"" + entity + "\"})- [rel:"+relation+"] -> (n2) RETURN n1,rel,TYPE(rel),n2")
		return answer

	#关系查询：关系+实体2
	def findOtherEntities2(self,entity,relation):
		print("findOtherEntities2==")
		print(entity,relation)
		answer = self.graph.run("MATCH (n1)- [rel:"+relation+"] -> (n2 {name:\"" + entity + "\"}) RETURN n1,rel,TYPE(rel),n2" ).data()
		return answer

	#关系查询：实体1+实体2
	def findRelationByEntities(self,entity1,entity2):
		answer = self.graph.run("MATCH (n1:`专家` {name:\"" + entity1 + "\"})- [rel] -> (n2 {name:\""+entity2+"\"}) RETURN n1,rel,TYPE(rel),n2" ).data()
		print("MATCH (n1:`专家` {name:\"" + entity1 + "\"})- [rel] -> (n2 {name:\""+entity2+" \"}) RETURN n1,rel,TYPE(rel),n2" )
		return answer

	#查询数据库中是否有对应的实体-关系匹配
	def findEntityRelation(self,entity1,relation,entity2):
		answer = self.graph.run("MATCH (n1:`专家` {name:\"" + entity1 + "\"})- [rel:"+relation+"] -> (n2) where n2.name=\""+entity2+"\" RETURN n1,rel,TYPE(rel),n2" ).data()
		print("MATCH (n1:`专家` {name:\"" + entity1 + "\"})- [rel:"+relation+"] -> (n2) where n2.name=\""+entity2+"\" RETURN n1,rel,TYPE(rel),n2")
		return answer
