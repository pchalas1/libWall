import math

class Vec3(object):	

	"""@author : Preetham Chalasani
	@brief : 3D Vector Class
	"""

	def __init__(self, *args):		

		"""Input can be a 3 values(x,y,z) or list of 3 values or a single value(x=y=z)
		@param args : list or 3 values of type [float,int or long] or a single value
		"""

		if len(args) == 1 and type(args[0]).__name__ == 'list':
			self.__x = float(args[0][0])
			self.__y = float(args[0][1])
			self.__z = float(args[0][2])			
			pass
		elif len(args) == 1 and type(args[0]).__name__ in ['float', 'int', 'long']:
			self.__x = float(args[0])
			self.__y = float(args[0])
			self.__z = float(args[0])
			pass
		elif len(args) == 3:		
			self.__x = float(args[0])
			self.__y = float(args[1])
			self.__z = float(args[2])
			pass

	def __add__(self,a):

		"""Vector addition with another vector
		@param a : Vector
		@return result : Vector
		"""

		if type(a).__name__ in ['long','int','float']:
			x = self.__x + a
			y = self.__y + a
			z = self.__z + a			
		elif type(a) is Vec3:
			x = self.__x + a.X()
			y = self.__y + a.Y()
			z = self.__z + a.Z()

		return(Vec3(x, y, z))

	def __sub__(self,a):

		"""Vector substraction with another vector
		@param a : Vector
		@return result : Vector
		"""

		if type(a).__name__ in ['long','int','float']:
			x = self.__x - a
			y = self.__y - a
			z = self.__z - a			
		elif type(a) is Vec3:
			x = self.__x - a.X()
			y = self.__y - a.Y()
			z = self.__z - a.Z()

		return(Vec3(x, y, z))
		
	def __mul__(self, a):

		"""Vector multiplication with another vector
		@param a : Vector
		@return result : Vector
		"""

		if type(a).__name__ in ['long','int','float']:
			x = self.__x * a
			y = self.__y * a
			z = self.__z * a			
		elif type(a) is Vec3:
			x = self.__x * a.X()
			y = self.__y * a.Y()
			z = self.__z * a.Z()

		return(Vec3(x, y, z))

	def __div__(self, a):

		"""Vector elment wise division with another vector
		@param a : Vector
		@return result : Vector
		"""

		if type(a).__name__ in ['long','int','float']:
			x = self.__x / a
			y = self.__y / a
			z = self.__z / a
		elif type(a) is Vec3:
			x = self.__x / a.X()
			y = self.__y / a.Y()
			z = self.__z / a.Z()
		return(Vec3(x, y, z))

	def __mod__(self,a):

		"""Vector element wise modulus with another vector
		@param a : Vector
		@return result : Vector
		"""

		if type(a).__name__ in ['long','int','float']:
			x = self.__x % a
			y = self.__y % a
			z = self.__z % a
		elif type(a) is Vec3:
			x = self.__x % a.X()
			y = self.__y % a.Y()
			z = self.__z % a.Z()
		return(Vec3(x, y, z))
		pass

	def mag(self):

		"""Magnitude of the vector
		@return value : int or float or long
		"""

		value = float(math.sqrt(pow(self.__x,2) + pow(self.__y,2) + pow(self.__z,2)))
		return value


	def __str__(self):
		return(str([self.__x, self.__y, self.__z]))	

	def __neg__(self):

		"""Negation of the Vector
		@return v : Vector
		"""

		return Vec3(-self.__x, -self.__y, -self.__z)

	def __abs__(self):

		"""Element wise absolute value of the Vector
		@return v : Vector
		"""

		return Vec3(abs(self.__x), abs(self.__y), abs(self.__z))		

	def __eq__(self, a):

		"""Check if the vector is equal to another vector
		@param a : Vector
		@return boolean
		"""

		return type(a) is type(self) and self.__x == a.X() and self.__y == a.Y() and self.__z == a.Z()
		pass	

	def __pow__(self,n):

		"""Return a vector [x,y,z] such that i = pow(i,n) where i = x,y,z
		@return v : Vector
		"""

		return Vec3(pow(self.__x,n), pow(self.__y,n), pow(self.__z,n))

	def __setitem__(self,key,value):		

		"""Set the key index of the vector with value where key = 0,1,2 \n
		Use : A[key] = value
		@param key : 0,1 or 2
		@param value : int, float, or long
		
		"""
		v = [self.__x,self.__y,self.__z]
		v[key] = value
		self.__updateValues(v)
		pass

	def __getitem__(self,key):

		"""Retrieves the value of the key index \n		
		@param key : 0,1 or 2
		@return A[key] : int, float or long
		"""

		v = [self.__x,self.__y,self.__z]
		return v[key]

	def __updateValues(self,vec):

		"""Update the vector with the input vector
		@param vec : Vector
		"""

		self.__x = vec[0]
		self.__y = vec[1]
		self.__z = vec[2]
