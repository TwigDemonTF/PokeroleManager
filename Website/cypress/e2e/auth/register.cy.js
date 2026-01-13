describe('Register Page', () => {
  beforeEach(() => {
    cy.visit('/Register');
  });

  it('loads the register page', () => {
    cy.contains('Register').should('be.visible');
    cy.get('form#registerForm').should('exist');
  });

  it('allows a user to register and redirects to login', () => {
    const username = `testuser_${Date.now()}`;
    const password = 'TestPassword123';

    cy.get('#username')
      .should('be.visible')
      .type(username);

    cy.get('#password')
      .should('be.visible')
      .type(password);

    cy.get('button[type="submit"]').click();

    // Flask redirects to /Login after successful POST
    cy.url().should('include', '/Login');
  });

  it('requires username and password', () => {
    cy.get('button[type="submit"]').click();

    // HTML5 validation should prevent submission
    cy.get('#username:invalid').should('exist');
    cy.get('#password:invalid').should('exist');
  });
});