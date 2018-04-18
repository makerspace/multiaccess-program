from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    
    __tablename__ = 'Users'
    
    id = Column("Id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column("Name", String(length=50), nullable=False, index=True)
    code = Column("Code", String(10))
    card = Column("Card", String(12))
    start_timestamp = Column("Start", DateTime(timezone=False))
    stop_timestamp = Column("Stop", DateTime(timezone=False))
    blocked = Column("Blocked", Boolean())
    f0 = Column("f0", String(50))
    f1 = Column("f1", String(50))
    f2 = Column("f2", String(50))
    f3 = Column("f3", String(50))
    f4 = Column("f4", String(50))
    f5 = Column("f5", String(50))
    f6 = Column("f6", String(50))
    f7 = Column("f7", String(50))
    f8 = Column("f8", String(50))
    f9 = Column("f9", String(50))
    f10 = Column("f10", String(50))
    f11 = Column("f11", String(50))
    f12 = Column("f12", String(50))
    f13 = Column("f13", String(50))
    f14 = Column("f14", String(50))
    fi0 = Column("fi0", Integer())
    fi1 = Column("fi1", Integer())
    fi2 = Column("fi2", Integer())
    fi3 = Column("fi3", Integer())
    changed = Column("Changed", Integer())
    customer_id = Column("customerId", ForeignKey("Customer.Id"), index=True)
    created_timestamp = Column("createdTime", DateTime(timezone=False))
    portal_name = Column("PortalName", String(50))
    password = Column("Password", String(50))
    portal_level = Column("PortalLevel", Integer())
    pul_block = Column("pulBlock", Boolean(), nullable=False, default=False)
    pt_first_name = Column("PTFirstName", String(50))
    pt_last_name = Column("PTLastName", String(50))


class Authority(Base):
    
    __tablename__ = 'Authority'
    
    id = Column("Id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column("Name", String(length=50))
    flags = Column("Flags",  Integer())
    auto_generated = Column("AutoGenerated", Boolean(), nullable=False, default=False)
    
    
class AuthorityInUser(Base):

    __tablename__ = 'AuthorityInUser'
    
    id = Column("Id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    user_id = Column("UserId", ForeignKey("Users.Id"), nullable=False)
    authority_id = Column("AuthorityId", ForeignKey("Authority.Id"), nullable=False)
    removed_date = Column("removeDate", DateTime(timezone=False))
    start_timestamp = Column("start", DateTime(timezone=False))
    stop_timestamp = Column("stop", DateTime(timezone=False))
    
    # Actually foreign key to Operators, but we don't touch that table and it is always Null.
    created_by = Column("CreatedBy",  Integer())
    
    
class Customer(Base):
    # This table is not complete but we will not manipulate the Customer table, just use it.
    
    __tablename__ = 'Customer'
    
    id = Column("Id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column("Name", String(length=50), nullable=False, index=True)


    