---
name: backend_java_springboot
description: Strict guidelines for Java Spring Boot development, focusing on SOLID, JPA, and architecture.
---

# Specialist Java Spring Boot & JPA

## 1. Architectural Design & Flow

- **Controllers:** All request/response handling must be strictly done in `RestController` classes.
- **Services:** All database and business logic must reside in `ServiceImpl` classes. RestControllers cannot autowire Repositories directly. ServiceImpl classes cannot query the DB directly; they must use `Repositories`.
- **Data Transfer (DTOs):** Data passing between Controllers and Services must be done strictly using DTOs.
- **Entities:** Entity classes must only be used to carry data out of database executions.

## 2. Entity Management

- Annotate entity classes with `@Entity` and `@Data` (Lombok).
- IDs must be annotated with `@Id` and `@GeneratedValue(strategy=GenerationType.IDENTITY)`.
- Use `FetchType.LAZY` for all relationships by default.
- Use proper validation annotations (e.g., `@Size`, `@NotEmpty`, `@Email`).

## 3. Repository (DAO)

- Interfaces must extend `JpaRepository` and be annotated with `@Repository`.
- Use JPQL for `@Query` methods.
- **N+1 Prevention:** Must use `@EntityGraph(attributePaths={"relatedEntity"})` in relationship queries.
- Use a DTO as the data container for multi-join queries.

## 4. Service Layer

- Create Service interfaces and corresponding `ServiceImpl` classes (annotated with `@Service`).
- Use Constructor injection or `@Autowired` appropriately. Return objects must be DTOs.
- Handle existence checks using repository methods with `.orElseThrow()`.
- Use `@Transactional` for sequential database executions.

## 5. REST Controllers & Error Handling

- Use resource-based routing (`@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`). Avoid verbs in paths (e.g., `/users/{id}`, not `/getUsers`).
- Methods must return `ResponseEntity<ApiResponse<T>>`.
- **Global Exception Handling:** Catch blocks must throw custom exceptions handled by a `@RestControllerAdvice` GlobalExceptionHandler. Never swallow errors.
