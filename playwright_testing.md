---
description: Playwright API testing guidelines and best practices using pw-api-plugin and Zod.
---

# Specialist API Testing (Playwright)

## 1. Core Principles

- **Auto-detect Environment:** Always verify if the project uses TypeScript (`tsconfig.json`) and adapt extensions and syntax accordingly.
- **Isolation:** Create isolated, deterministic tests that do not rely on existing server state.
- **Validation:** Use `pw-api-plugin` to make and validate API requests.

## 2. Best Practices

- **Descriptive Names:** Use test names that clearly describe the API functionality being tested.
- **Request Organization:** Group API tests by endpoint using `test.describe` blocks.
- **Response Validation:** Validate both status codes and response body content strictly.
- **Error Handling:** Test both successful scenarios (happy paths) and expected error conditions (e.g., 401 Unauthorized, 400 Bad Request).
- **Schema Validation:** Validate response structure against expected schemas using `Zod`.

## 3. Example Implementation

Use the `api` object from `pw-api-plugin` and `zod` for robust schema parsing:

```typescript
import { test, expect } from '@playwright/test';
import { api } from 'pw-api-plugin';
import { z } from 'zod';

const userSchema = z.object({
  id: z.number(),
  name: z.string(),
  email: z.string().email(),
});

test.describe('Users API', () => {
  test('should return 201 and create user', async () => {
    const response = await api.post('/api/users', { data: { name: 'Test' } });
    expect(response.status()).toBe(201);
    
    const data = await response.json();
    expect(userSchema.safeParse(data).success).toBeTruthy();
  });
});
```
