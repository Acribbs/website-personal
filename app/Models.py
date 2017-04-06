from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user,\
    current_user
from flask_bcrypt import Bcrypt
from oauth import OAuthSignIn
from app import app
from datetime import datetime

db = SQLAlchemy(app)

#Password hashing
bcrypt = Bcrypt(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    
class csvdb(db.Model):
	__bind_key__ = 'csvdb'
	rowid = db.Column(db.Integer, primary_key=True)
	CRISPR = db.Column(db.String)
	Chr = db.Column(db.String)
	Gene = db.Column(db.String)
	Constituitive = db.Column(db.String)
	Conserv_Score = db.Column(db.Integer)
	cut_site = db.Column(db.Integer)
	Start_feature = db.Column(db.Integer)
	End_feature = db.Column(db.Integer)
	Dist_start = db.Column(db.Integer)
	Dist_End = db.Column(db.Integer)
	OffScores = db.Column(db.Integer)
	On_target_score1 = db.Column(db.Integer)
	On_target_score2 = db.Column(db.Integer)
	On_target_score3 = db.Column(db.Integer)
	SNP_Count = db.Column(db.Integer)
	PercentGC = db.Column(db.Integer)
	TTTT = db.Column(db.String)
	TwentyFourMer = db.Column(db.String)
	Exon_number = db.Column(db.String)
	strand = db.Column(db.String)
	
	def __init__(self, rowid, CRISPR, Chr, Gene,\
	Constituitive, Conserv_Score, cut_site,Start_feature, End_feature,\
	Dist_start, Dist_End, OffScores,On_target_score1,\
	On_target_score2, On_target_score3, SNP_Count, PercentGC,TTTT, TwentyFourMer, Exon_number, strand):
	
		self.rowid = rowid
		self.CRISPR = CRISPR
		self.Chr = Chr
		self.Gene = Gene
		self.Constituitive = Constituitive
		self.Conserv_Score = Conserv_Score
		self.cut_site = cut_site
		self.Start_feature = Start_feature
		self.End_feature = End_feature
		self.Dist_start = Dist_start
		self.Dist_End = Dist_End
		self.OffScores = OffScores
		self.On_target_score1 = On_target_score1
		self.On_target_score2 = On_target_score2
		self.On_target_score3 = On_target_score3
		self.SNP_Count = SNP_Count
		self.PercentGC = PercentGC
		self.TTTT = TTTT
		self.TwentyFourMer = TwentyFourMer
		self.Exon_number = Exon_number
		self.strand = strand
	
		
	def __repr__(self):
		return "<csvdb(%r, %r, %r)" % (self.rowid, self.CRISPR, self.cut_site)
		
class User2(UserMixin, db.Model):
    __tablename__ = "users2"
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20), unique=True , index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True , index=True)
    registered_on = db.Column(db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.registered_on = datetime.utcnow()
    
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User2 %r>' % (self.username)
