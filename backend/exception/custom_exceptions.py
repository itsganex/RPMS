class RPMSException(Exception): pass
class CandidateNotFoundError(RPMSException): pass
class JobNotFoundError(RPMSException): pass
class DuplicateApplicationError(RPMSException): pass
class CandidateNotEligibleError(RPMSException): pass
class InvalidTransitionError(RPMSException): pass
class AuthenticationError(RPMSException): pass
class ValidationError(RPMSException): pass
