from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Episodio(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.DurationField()
    data_disponibilizac = models.DateTimeField()

    def __str__(self):
        return f'{self.nome}{self.duracao}{self.data_disponibilizac}'

class Ator(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=70)
    insta = models.CharField(max_length=20)
    face = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} {self.site} {self.insta} {self.face} {self.twitter} {self.nacionalidade}'

class Diretor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=70)
    insta = models.CharField(max_length=20)
    face = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} {self.site} {self.insta} {self.face} {self.twitter} {self.nacionalidade}'

    
class Temporada(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Continente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Pais(models.Model):
    nome = models.CharField(max_length=30)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.continente}'
    
class Filme(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.DurationField()
    sinopse = models.CharField()
    site_oficial = models.CharField(max_length=50)
    data_lancamento = models.DateTimeField()
    nota_avaliacao = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site_oficial} {self.data_lancamento} {self.nota_avaliacao} {self.categoria} {self.pais} {self.diretor}'

class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.filme}{self.ator}'
    
class Serie(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.DurationField()
    sinopse = models.CharField()
    site_oficial = models.CharField(max_length=50)
    data_lancamento = models.DateTimeField()
    nota_avaliacao = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site_oficial} {self.data_lancamento} {self.nota_avaliacao} {self.categoria} {self.pais} {self.diretor}'
    
class SerieEpisodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serie} {self.temporada} {self.episodio}'
    


