class RDP_Vuln:

	def __init__(self, ip, port, os, ssl_dhparams_key, ssl_data_key, organization, city):
		self.ip = ip
		self.port = port
		self.os = os
		self.ssl_dhparams_key = ssl_dhparams_key
		self.ssl_data_key = ssl_data_key
		self.organization = organization
		self.city = city

	def to_dict(self):
		return {
			'ip': self.ip,
			'port': self.port,
			'os': self.os,
			'ssl_dhparams_key_lengh': self.ssl_dhparams_key,
			'ssl_data_key_lengh': self.ssl_data_key,
			'organization': self.organization,
			'city': self.city,
		}


class nginx_Vuln:

	def __init__(self, ip, port, version, organization, city):
		self.ip = ip
		self.port = port
		self.version = version
		self.organization = organization
		self.city = city

	def to_dict(self):
		return {
			'ip': self.ip,
			'port': self.port,
			'vesion': self.version,
			'organization': self.organization,
			'city': self.city,
		}