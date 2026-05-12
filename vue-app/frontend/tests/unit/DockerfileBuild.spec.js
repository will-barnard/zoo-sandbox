import { execSync } from 'child_process';

describe('Dockerfile Build', () => {
  it('should build the frontend image using the correct Dockerfile', () => {
    const output = execSync('docker-compose -f docker-compose.yml build --no-cache frontend').toString();
    expect(output).toContain('Step 1/8 : FROM node:14');
    expect(output).toContain('Successfully built');
  });
});