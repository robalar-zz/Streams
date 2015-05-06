from nose.tools import assert_equals

def setup_module(module):
    print ''
    print 'Setting up module'

def teardown_module(module):
    print 'Tearing down module'
    
def test_sample():
    print '3 * 4 == 12'
    assert_equals(3 * 4 == 12)