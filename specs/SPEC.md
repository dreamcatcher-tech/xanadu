# Xanadu Requirements Specification

## 1. Global Address Space
- Every object in Udanax Green has a unique global address called a tumbler【F:md/green/febe/addressing.md†L11-L24】.
- Addresses exist for nodes, accounts, documents, and even individual characters and links【F:md/green/febe/addressing.md†L48-L72】.
- Complex sets of objects can be identified with spans, vspans, and spec-sets【F:md/green/febe/addressing.md†L80-L106】.

## 2. Rich Linking Model
- Links support extremely fine-grained and complex connections, interpreted by frontends and preserved across edits【F:md/green/febe/implementation.md†L31-L44】.
- A link can connect any set of objects across document boundaries and is stored in a home document independent of what it connects【F:md/green/febe/overview.md†L75-L90】.

## 3. Versioning and Document Comparison
- Opening a document for writing may create a virtual copy so parallel versions can be edited independently and later compared【F:md/green/febe/versions.md†L21-L68】.
- The version comparison operation applies to any byte data and avoids heuristic diffing by tracing intentional sharing【F:md/green/febe/versions.md†L70-L77】.

## 4. FeBe Protocol
- Frontends and backends communicate over the FeBe protocol as described in the manual【F:md/green/index.md†L18-L24】.
- The backend handles storage, linking, editing, versioning, information retrieval, access control, and multi-user access【F:md/green/febe/overview.md†L31-L45】.

## 5. Multi-User Collaboration
- Contention between frontends is resolved through automatic version creation so multiple users can interact with the same backend simultaneously【F:md/green/febe/overview.md†L153-L167】.

## 6. Scalability (Unbounded Information Pools)
- The system is designed for information pools of unlimited size and avoids moving large segments during edits to keep working as it scales【F:md/green/febe/implementation.md†L236-L260】.

## 7. Preservation of Context
- Xanadu aims to maintain webs of context around information rather than treating documents as isolated islands【F:md/green/febe/philosophy.md†L12-L31】【F:md/green/febe/philosophy.md†L96-L146】.
- Diversity and pluralism are encouraged so multiple paths to knowledge can coexist and cross-fertilize【F:md/green/febe/philosophy.md†L180-L212】.

## 8. Open Licensing
- Udanax Green and Udanax Gold are "hereby open-sourced under the MIT X-11 License"【F:md/license.md†L14-L16】.
- The license grants rights to use, copy, modify, merge, publish, and distribute the software【F:md/license.md†L46-L50】.

## 9. Legacy and Future Work
- Udanax Gold (Xanadu 92.1) contains more ambitious code including General Enfilade Theory and The Ent and is released as prior art【F:md/gold/index.md†L16-L32】.
- The available download files are Smalltalk fileouts not yet usable without heroic effort due to the custom XTalk/X++ system【F:md/gold/download/index.md†L19-L27】.

## 10. Supplement from General Knowledge
- Historically, Xanadu also envisioned transclusion (quoting by reference rather than copy) and micropayments for content. These ideas are well known from Ted Nelson's writings but not detailed in the repository.
