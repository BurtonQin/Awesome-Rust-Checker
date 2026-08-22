# Awesome Rust Analysis & Verification

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Contributions welcomed! Last updated: 2026-08-21

A curated list of awesome Rust analysis and verification tools, including linters, static analyzers, dynamic analyzers, formal verifiers, and security tooling.

## Table of contents

- [Linters](#linters)
- [Static Checkers](#static-checkers)
- [Dynamic Checkers](#dynamic-checkers)
- [Verifiers](#verifiers)
- [Dependency & Supply Chain Security](#dependency--supply-chain-security)
- [Academic Papers](#academic-papers)

---

## Linters

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [clippy](https://github.com/rust-lang/rust-clippy) | A bunch of lints to catch common mistakes and improve your Rust code. Paper: [ICSE-Companion'24](https://dl.acm.org/doi/abs/10.1145/3639478.3643096) | HIR | Versatile | Pattern matching | 2026-08-20 |
| [dylint](https://github.com/trailofbits/dylint) | Run Rust lints from dynamic libraries | HIR | Versatile | Pattern matching | 2026-08-15 |
| [snarf](https://github.com/cong-or/snarf) | Cache-line false sharing linter for Rust structs — detects potential cache-line false sharing by finding cases where atomic or contended fields share a cache line | Source Code | Cache-line false sharing (performance) | Layout analysis | 2026-05-25 |
| [redpen](https://github.com/estebank/redpen) | A Rust code linter operating as rustc_driver; currently implements `dont_panic` and `disallow` lints with cross-crate panic reachability tracking | HIR, MIR | Panic reachability, Type parameter restrictions | Pattern matching | 2024-06-10 |

---

## Static Checkers

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------|-----------| ----------- |
| [MIRAI](https://github.com/endorlabs/MIRAI) | Rust mid-level IR Abstract Interpreter, Paper: [arxiv](https://arxiv.org/pdf/2607.01504) | MIR | Panic, Security bugs, Correctness | Abstract Interpretation | 2025-03-04 |
| [lockbud](https://github.com/BurtonQin/lockbud) | Statically detect common memory and concurrency bugs in Rust. Paper: [Safety Issues in Rust, TSE'24](https://songlh.github.io/paper/rust-tse.pdf) | MIR | Double-Lock, Conflicting-Lock-Order, Atomicity-Violation, Use-After-Free, Invalid-Free, Panic Locations | Data-flow Analysis | 2026-07-21 |
| [RAPx](https://github.com/safer-rust/RAPx) | This is a static analysis project for analyzing Rust program. Paper: [SafeDrop, TOSEM'22](https://dl.acm.org/doi/10.1145/3542948), [RCanary, TSE'24](https://arxiv.org/pdf/2308.04787) | HIR, MIR | Use-After-Free, Memory Leakage | Static Program Analysis, Model Checking | 2026-08-20 |
| [safety-tags](https://github.com/safer-rust/safety-tags) | Tag the safety properties of the Rust standard library. Paper: [arxiv](https://arxiv.org/pdf/2504.21312) | Source Code | Unsafe | Annotation | 2026-08-02 |
| [Rudra](https://github.com/sslab-gatech/Rudra) | Rust Memory Safety & Undefined Behavior Detection. Paper: [Rudra, SOSP'21](https://dl.acm.org/doi/abs/10.1145/3477132.3483570) | HIR, MIR | Memory safety when panicked, Higher Order Invariant, Send Sync Variance | Data-flow Analysis | 2026-04-02 |
| [Yuga](https://github.com/vnrst/Yuga) | Automatically Detecting Lifetime Annotation Bugs in the Rust Language. Paper: [Yuga, ICSE'24](https://arxiv.org/abs/2310.08507) | HIR, MIR | Lifetime Annotation Bugs | Data-flow Analysis | 2024-04-01 |
| [MirChecker](https://github.com/lizhuohua/rust-mir-checker) | A Simple Static Analysis Tool for Rust. Paper: [MirChecker, CCS'21](https://dl.acm.org/doi/10.1145/3460120.3484541) | MIR | Panic (including numerical), Lifetime Corruption (memory issues) | Abstract Interpretation | 2024-05-24 |
| [FFIChecker](https://github.com/lizhuohua/rust-ffi-checker) | A Static Analysis Tool For Detecting Memory Management Bugs Between Rust and C/C++. Paper: [FFIChecker, ESORICS'22](https://dl.acm.org/doi/10.1007/978-3-031-17143-7_33) | LLVM IR | Memory issues across the Rust/C FFI | Abstract Interpretation | 2022-05-31 |
| [RUPTA](https://github.com/rustanlys/rupta) | Supports pointer/alias analysis for Rust, operating on Rust MIR. It currently offers callsite-based pointer analysis. Paper: [RUPTA, CC'24](https://dl.acm.org/doi/10.1145/3640537.3641574), [Stack Filtering, CGO'25](https://dl.acm.org/doi/pdf/10.1145/3696443.3708921) | MIR | Not bugs, for callgraph construction | Callsite-based pointer analysis | 2026-07-13 |
| [Pincer](https://github.com/rustanlys/pincer) | Static analyzer for unsafe Rust memory-safety bugs. Paper: [Pincer, OOPSLA'26](https://dl.acm.org/doi/abs/10.1145/3798266) | MIR | Use-after-free, Double-free, Dangling pointer | Demand-driven IFDS alias analysis, Typestate analysis | 2026-04-14 |
| [Cocoon](https://github.com/PLaSSticity/Cocoon-implementation) | Static Information Flow Control in Rust. Paper: [Cocoon, OOPSLA'24](https://dl.acm.org/doi/pdf/10.1145/3649817) | Rust Source Code | Secrecy Leaks | Rust's type system and procedural macros | 2024-03-20 |
| [rustsp_analyzer](https://github.com/Artisan-Lab/rustsp_analyzer) | Fearless Unsafe. A More User-friendly Document for Unsafe Rust Programming Base on Refined Safety Properties. Paper: [Fearless Unsafe](https://arxiv.org/pdf/2412.06251) | HIR | Safety Properties | Summarization | 2025-01-01 |
| [AtomVChecker](https://github.com/AtomVChecker/rust-atomic-study/tree/main/section-5-detection/AtomVChecker) | Statically detect memory ordering misuses for Rust. Paper: [AtomVChecker, ISSRE'24](https://ieeexplore.ieee.org/document/10771495) | MIR | Atomic concurrency bugs and performance loss due to memory ordering misuse | Data-flow Analysis | 2025-06-27 |
| [rustowl](https://github.com/cordx56/rustowl) | Visualize ownership and lifetimes in Rust for debugging and optimization | MIR | Lifetime Errors | Rust's borrow checker | 2026-08-17 |
| [cargo-pinch(pinchecker)](https://github.com/yxdai-nju/pinchecker) | Contract Violation detection tool for Rust crates. Paper: [PinChecker, arxiv](https://arxiv.org/abs/2504.14500) | MIR, [PLIR](https://github.com/yxdai-nju/mir2rpil) | unsafe code that fails to uphold its safety requirements (Pin-related memory bugs for now) | - | 2025-03-04 |
| [mirilli](https://github.com/icmccorm/mirilli) | A study of undefined behavior across foreign function boundaries in Rust libraries | MIR, LLVM IR | UB across FFI boundaries | - | 2025-02-13 |
| [TypePulse](https://github.com/shinmao/TYPEPULSE) | TypePulse: Detecting Type Confusion Bugs in Rust Programs. Paper: [TypePulse, USENIX Security'25](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-952-chen-hung-mao.pdf) | MIR | Type confusion | Type conversion & pointer alias analysis | 2025-12-13 |
| [Rust-API-Bypass-Checker](https://github.com/Rust-API/Rust-API-Bypass-Checker) | A conservative MIR-based static analysis tool that identifies redundant safety checks in Rust programs to improve performance | MIR | Redundant safety checks | Interval analysis | 2026-05-22 |
| [the-janitor](https://github.com/janitor-security/the-janitor) | Rust static-analysis security research platform for IFDS, Z3/Kani proof obligations, exploit-witness generation | MIR, LLVM IR | Security vulnerabilities, Memory safety | Static Analysis, Symbolic Execution | 2026-08-10 |
| [Crema](https://github.com/AFx3/crema-static-analyzer) | Static analysis tool for Rust-C FFI detecting memory leaks, double-free and use-after-free in pure unsafe Rust and Rust-C interaction. Paper: [SEFM'25](https://doi.org/10.1007/978-3-032-10444-1_11) | LLVM IR (SVF) | Memory leak, Double-free, Use-after-free (FFI) | Static Value-Flow Analysis | 2025-12-06 |
| [Rust-IR-BERT](https://github.com/Boshra-01/Rust-IR-BERT) | Machine Learning-Based Vulnerability Detection in Rust Code Using LLVM IR and Transformer Model. Paper: [Machine Learning and Knowledge Extraction](https://www.mdpi.com/2504-4990/7/3/79) | Source Code, LLVM IR | Vulnerabilities | BERT | 2025-10-20 |

---

## Dynamic Checkers

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [miri](https://github.com/rust-lang/miri) | An interpreter for Rust's mid-level intermediate representation. Paper: [Miri: Practical Undefined Behavior Detection for Rust, POPL'26](https://dl.acm.org/doi/abs/10.1145/3776690) | MIR | Undefined Behavior | Concrete Interpretation / Dynamic Analysis | 2026-08-20 |
| [BorrowSanitizer](https://github.com/borrowSanitizer/bsan) | Work-in-progress LLVM instrumentation pass for detecting aliasing violations in multi-language Rust applications. | LLVM IR | Borrowing/Aliasing Model Violations | LLVM Instrumentation, Shadow Memory | 2026-08-18 |
| [cargo-careful](https://github.com/RalfJung/cargo-careful) | Execute Rust code carefully, with extra checking along the way | - | Undefined Behavior | Enable Debug Assertion in std | 2026-08-08 |
| [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) | Command line helpers for fuzzing | Binary | Crashes, Panics, Memory errors | Fuzzing | 2026-07-20 |
| [Loom](https://github.com/tokio-rs/loom) | Concurrency permutation testing tool for Rust. | Source Code | Concurrency Bugs | Permutation testing | 2026-02-20 |
| [Shuttle](https://github.com/awslabs/shuttle) | A library for testing concurrent Rust code. Paper: [A Randomized Scheduler with Probabilistic Guarantees of Finding Bugs](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/asplos277-pct.pdf) | Source Code | Concurrency Bugs | Randomized testing | 2026-08-20 |
| [ERASAN](https://github.com/S2-Lab/ERASan) | Efficient Rust Address Sanitizer. Paper: [IEEES&P'24](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a239/1WPcYZde4BW) | - | Memory Access Bugs | Fuzzing | 2025-06-30 |
| [Automated-Fuzzer](https://github.com/qarmin/Automated-Fuzzer) | Simple tool to create broken files and checking them with special apps | - | Panic | Fuzzing | 2026-06-26 |
| [RULF](https://github.com/Artisan-Lab/RULF) | Fuzz Target Generator for Rust libraries. Paper: [RULF, ASE'21](https://dl.acm.org/doi/abs/10.1109/ASE51524.2021.9678813) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | 2023-11-09 |
| [RPG](https://github.com/wcventure/PERIOD)<sup>1</sup> | RPG: Rust Library Fuzzing with Pool-based Fuzz Target. Paper: [RPG, ICSE'24](https://dl.acm.org/doi/10.1145/3597503.3639102) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | 2022-10-09 |
| [SyRust](https://kilthub.cmu.edu/articles/code/SyRust_Artifact_PLDI2021_Artifact/14356976) | Automatic Testing of Rust Libraries with Semantic-Aware Program Synthesis. Paper: [SyRust, PLDI'21](https://dl.acm.org/doi/pdf/10.1145/3453483.3454084) | - | - | Program Synthesis | 2021-04-14 |
| [NADER](https://zenodo.org/records/5484436) | Automatic Context-Aware Safety Enhancement for Rust. Paper: [OOPSLA'21](https://dl.acm.org/doi/pdf/10.1145/3485480) | MIR, Source Code | Unchecked Indexing | API Replacing | 2021-07-13 |
| [casr](https://github.com/ispras/casr)<sup>2</sup> | collect crash (or UndefinedBehaviorSanitizer error) reports, triage, and estimate severity. Paper: [Casr-Cluster, ISPRAS'21](https://www.doi.org/10.1109/ISPRAS53967.2021.00012), [Ivannikov Memorial Workshop'24](https://arxiv.org/abs/2405.18174) | Crash Reports from ASan, UBSan, GDB | - | Analyze crashes | 2026-05-30 |
| [rustsmith](https://github.com/rustsmith/rustsmith) | A randomized program fuzzer for the Rust programming language. Paper: [rustsmith, ISSTA'23](https://rustsmith.github.io/docs/rustsmith-paper.pdf) [rustsmith, thesis](https://rustsmith.github.io/docs/rustsmith-thesis.pdf) | AST | Rust compiler bugs | Differential testing | 2023-07-21 |
| [rustlantis](https://github.com/cbeuw/rustlantis) | UB-free and deterministic rustc fuzzer. Paper: [rustlantis, OOPSLA'24](https://dl.acm.org/doi/pdf/10.1145/3689780) | MIR | Rust compiler bugs | Differential testing | 2025-11-15 |
| [RuMono](https://github.com/Artisan-Lab/RULF/tree/RuMono) | A fully automated Rust fuzz driver generator. Paper: [RuMono, TOSEM'24](https://dl.acm.org/doi/abs/10.1145/3709359) | - | Generic APIs | Fuzzing | 2023-11-09 |
| [rtsan-standalone-rs](https://github.com/realtime-sanitizer/rtsan-standalone-rs) | Standalone RealtimeSanitizer for Rust. [Blogpost](https://steck.tech/posts/rtsan-in-rust/) | Source Code | Real-time Violations | Instrumentation | 2025-09-27 |
| [RustSan](https://github.com/sslab-skku/RustSan) | RustSan: Retrofitting AddressSanitizer for Efficient Sanitization of Rust. Paper: [USENIX Security'24](https://www.usenix.org/conference/usenixsecurity24/presentation/cho-kyuwon) | LLVM IR | Memory bugs | Instrumentation | 2024-10-11 |
| [SafeFFI](https://zenodo.org/records/18940953) | Efficient Sanitization at the Boundary Between Safe and Unsafe Code in Rust and Mixed-Language Applications [USENIX Security'26](https://www.plai.ifi.lmu.de/publications/usenixsecurity26-safeffi.pdf) [NDSS'24 Poster](https://www.ndss-symposium.org/wp-content/uploads/ndss24-posters-37.pdf) | MIR, LLVM IR | Memory safety in C/C++ and Rust Mixed Code | Instrumentation | 2026-03-10 |
| [Hopper](https://github.com/FuzzAnything/Hopper) | Hopper is a tool for generating fuzzing test cases for libraries automatically using interpretative fuzzing | Binary | Library API bugs | Fuzzing | 2026-05-16 |
| [dhat-rs](https://github.com/nnethercote/dhat-rs) | Heap profiling and ad hoc profiling for Rust programs | - | Memory leaks, Heap allocation patterns | Instrumentation | 2025-02-20 |
| [afl.rs](https://github.com/rust-fuzz/afl.rs) | Fuzzing Rust code with American Fuzzy Lop | Binary | Memory corruption, Panics, Crashes | Fuzzing (AFL) | 2026-08-06 |
| [LibAFL](https://github.com/AFLplusplus/LibAFL) | Advanced Fuzzing Library - Slot your Fuzzer together in Rust! Scales across cores and machines. [PR#981](https://github.com/AFLplusplus/LibAFL/pull/981) from Paper: [CrabSandwich, Fuzzing'23](https://dl.acm.org/doi/abs/10.1145/3605157.3605176). See [issue#5](https://github.com/CodeSentryAI/Awesome-Rust-Checker/issues/5) | Binary | Memory corruption, Panics, Crashes | Fuzzing Framework | 2026-08-18 |
| [test-fuzz](https://github.com/trailofbits/test-fuzz) | To make fuzzing Rust easy - automated fuzz target generation | Source Code | Panics, Crashes | Fuzzing | 2026-08-13 |
| [fuzzcheck-rs](https://github.com/loiclec/fuzzcheck-rs) | Modular, structure-aware, and feedback-driven fuzzing engine for Rust functions | Source Code | Panics, Crashes | Fuzzing | 2026-01-22 |
| [honggfuzz-rs](https://github.com/rust-fuzz/honggfuzz-rs) | Fuzz your Rust code with Google-developed Honggfuzz | Binary | Memory corruption, Panics | Fuzzing (Honggfuzz) | 2026-08-04 |
| [deepSURF](https://github.com/purseclab/deepSURF) | deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses. Paper: [IEEE S&P'26](https://arxiv.org/abs/2506.15648) | HIR, MIR | Memory Bugs | Hybrid, LLM | 2025-11-28 |
| [mutest-rs](https://github.com/zalanlevai/mutest-rs) | Flexible, Efficient Mutation Analysis Tool for Rust Programs, using Extensive Static Analysis. Paper: [ICST'26](https://conf.researchr.org/details/icst-2026/icst-2026-testing-tools-and-data-showcase/2/mutest-rs-Flexible-Efficient-Mutation-Analysis-Tool-for-Rust-Programs-using-Extens) | rustc internals, MIR | Test-suite inadequacy, Surviving mutants | Static Analysis, Mutation Analysis | 2026-01-01 |
| [rl-guided-static-analysis-rust](https://github.com/Akileshdash/rl-guided-static-analysis-rust) | A reinforcement learning–guided framework for reducing false positives in static memory safety analysis of Rust programs. Paper: [P Akilesh](https://arxiv.org/abs/2605.04000) | MIR | Reduce FPs of Memory Bugs | Hybrid, RL | 2026-01-26 |

1. The link may be incorrect. See [here](https://wcventure.github.io/EnPage/opensource/2023-12-05-RPG).
2. casr analyze the results of dynamic checkers instead of performing dynamic analysis itself. Thanks [zjp-CN](https://github.com/zjp-CN) for recommending casr.

---

## Verifiers

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [kani](https://github.com/model-checking/kani/) | The Kani Rust Verifier is a bit-precise model checker for Rust. Paper: [kani, ICSE-SEIP'22](https://dl.acm.org/doi/abs/10.1145/3510457.3513031) | MIR | Memory safety, User-specified assertions, Panics, Unexpected behavior (e.g., arithmetic overflows) | Model Checking | 2026-08-20 |
| [prusti](https://github.com/viperproject/prusti-dev) | A static verifier for Rust, based on the Viper verification infrastructure. Paper: [prusti, NFM'22](https://link.springer.com/chapter/10.1007/978-3-031-06773-0_5) | Viper | Panic (including arithmetic), User-specified assertions | Symbolic Execution | 2024-03-26 |
| [crux-mir](https://github.com/GaloisInc/crucible/tree/master/crux-mir) | A static simulator for Rust programs. Paper: [crux](https://arxiv.org/abs/2410.18280) | - | - | Symbolic Testing | 2026-08-18 |
| [verus](https://github.com/verus-lang/verus) | Verified Rust for low-level systems code. Paper: [verus, OOPSLA'23](https://dl.acm.org/doi/pdf/10.1145/3586037), [SOSP'24](https://www.microsoft.com/en-us/research/publication/verus-a-practical-foundation-for-systems-verification/) | - | - | SMT-based Verification | 2026-08-21 |
| [AutoVerus](https://github.com/microsoft/verus-proof-synthesis) | Automated proof generation system for Rust/Verus code. Paper: [autoverus, OOPSLA'25](https://dl.acm.org/doi/abs/10.1145/3763174) | - | - | LLM, SMT-based Verification | 2026-06-02 |
| [flux](https://github.com/flux-rs/flux) | flux is a refinement type checker for Rust. Paper: [flux, PLDI'23](https://dl.acm.org/doi/10.1145/3591283) | - | - | - | 2026-08-18 |
| [Aeneas](https://github.com/AeneasVerif/aeneas) | A verification toolchain for Rust programs. Paper: [Aeneas, ICFP'22](https://dl.acm.org/doi/abs/10.1145/3547647), [ICFP'24](https://dl.acm.org/doi/abs/10.1145/3674640) | LLBC (for safe Rust only) | - | - | 2026-08-20 |
| [hax](https://github.com/cryspen/hax) | A Rust verification tool. [Publications](https://hax.cryspen.com/publications.html) | - | Panic, Properties, Data Invariants | Translation to F* or Rocq | 2026-08-20 |
| [RustBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/) | Formal (and machine-checked) safety proof for a language representing a realistic subset of Rust. Paper: [RustBelt, POPL'18](https://dl.acm.org/doi/10.1145/3158154) | 𝜆Rust | - | - | 2024-12-13 |
| [RustHorn](https://github.com/hopv/rust-horn) | A CHC-based automated verifier for Rust [RustHorn, TOPLAS'21](https://dl.acm.org/doi/full/10.1145/3462205) | MIR | - | - | 2024-08-27 |
| [Creusot](https://github.com/creusot-rs/creusot) | A deductive verifier for Rust code. [Creusot, ICFEM'22](https://inria.hal.science/hal-03737878/file/main.pdf) | WhyML | Panics, overflows, Assertion failures | Deductive Verification | 2026-08-20 |
| [RustHornBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/-/tree/masters/rusthornbelt) | A Semantic Foundation for Functional Verification of Rust Programs with Unsafe Code. Paper: [RustHornBelt, PLDI'22](https://dl.acm.org/doi/10.1145/3519939.3523704) | 𝜆Rust | - | - | 2023-02-14 |
| [VerusBelt](https://zenodo.org/records/19613067) | A Semantic Foundation for Verus's Proof-Oriented Extensions to the Rust Type System. Paper: [VerusBelt, PLDI'26](https://iris-project.org/pdfs/2026-pldi-verusbelt.pdf), [Artifact](https://zenodo.org/records/19613067) | Rocq, Iris | Soundness of Verus proof-oriented extensions | Semantic Foundation | 2026-03-18 |
| [RefinedRust<sup>1</sup>](https://gitlab.mpi-sws.org/lgaeher/refinedrust-dev) | A Type System for High-Assurance Verification of Rust Programs. Paper: [RefinedRust, PLDI'24](https://dl.acm.org/doi/10.1145/3656422) | Radium | - | - | 2025-01-03 |
| [VeriFast<sup>2</sup>](https://github.com/verifast/verifast) | Research prototype tool for modular formal verification of C and Java programs. Paper: [VeriFast, NFM'11](https://doi.org/10.1007/978-3-642-20398-5_4) | - | - | Symbolic Execution | 2026-05-10 |
| [mendel-verifier](https://github.com/viperproject/mendel-verifier) | Capability-based verifier for safe Rust clients of interior mutability. Paper: [Poli](https://arxiv.org/abs/2405.08372), [Thesis](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/703796/Poli2024.pdf?sequence=3&isAllowed=y) | Viper | Interior Mutability | Symbolic Execution | 2024-07-16 |
| [silver-sif-extension](https://github.com/viperproject/silver-sif-extension) | Extension of the Viper language with modular product programs and information flow specifications. Paper: [Thesis](https://ethz.ch/content/dam/ethz/special-interest/infk/chair-program-method/pm/documents/Education/Theses/Till_Arnold_MA_Report.pdf) | Viper | Differential Privacy | Symbolic Execution | 2026-01-23 |
| [soteria-rust](https://github.com/soteria-tools/soteria) | Rust symbolic execution engine built with Soteria's functional symbolic-execution library, with Rust aliasing modeled using Tree Borrows. Paper: [Soteria, PLDI'26](https://pldi26.sigplan.org/details/pldi-2026-papers/63/Soteria-Efficient-Symbolic-Execution-as-a-Functional-Library) | ULLBC (generated by Obol or Charon) | Memory safety, Panics, Aliasing violations, Undefined Behavior | Symbolic Execution, Tree Borrows | 2026-08-22 |
| [mir-semantics](https://github.com/runtimeverification/mir-semantics) | KMIR: executable formal semantics of Rust Stable MIR in the K Framework, enabling execution, symbolic reasoning, and proofs over MIR programs | Stable MIR, K | Semantic violations, User-specified properties | Executable Formal Semantics, Symbolic Execution, Reachability Logic | 2026-07-27 |
| [cuq](https://github.com/neelsomani/cuq) | Cuq: A MIR-to-Coq Framework Targeting PTX for Formal Semantics and Verified Translation of Rust GPU Kernels | MIR, Coq | GPU kernel-level bugs | Translate MIR to Coq for PTX semantics | 2026-07-18 |
| [chronicle](https://github.com/elide-tools/chronicle) | MIR-based formal model extraction for Rust concurrent systems — TLA+ codegen & model checking | MIR | Concurrency bugs | Model extraction + TLA+ | 2026-03-18 |
| [seer](https://github.com/dwrensha/seer) | Symbolic execution engine for Rust | MIR | Panics, unreachable!(), assertion failures | Symbolic Execution | 2018-07-17 |
| [haybale](https://github.com/PLSysSec/haybale) | Symbolic execution of LLVM IR with an engine written in Rust | LLVM IR | Memory errors, UB | Symbolic Execution | 2023-10-27 |
| [rure](https://github.com/2over12/rure) | Reliable Unsafe Rust Engine — POC symbolic execution over unsafe Rust | MIR | Unsafe code bugs | Symbolic Execution | 2019-04-26 |

1. Thanks to [jedbrown](https://users.rust-lang.org/u/jedbrown) for recommending RefinedRust and other Rust-related verification tools.
2. Rust support is WIP in VeriFast. Thanks [zjp-CN](https://github.com/zjp-CN) for recommending VeriFast.

---

## Dependency & Supply Chain Security

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [cargo-deny](https://github.com/EmbarkStudios/cargo-deny) | Cargo plugin for linting your dependencies. Checks for security advisories, licenses, and banned crates | Cargo.lock, Source | Dependency vulnerabilities, License violations, Banned crates | Dependency Analysis | 2026-08-20 |
| [cargo-audit](https://github.com/rustsec/cargo-audit) | Audit Cargo.lock files for crates with security vulnerabilities reported to the RustSec Advisory Database | Cargo.lock | Known vulnerabilities in dependencies | Advisory Database Lookup | 2026-08-13 |
| [cargo-geiger](https://github.com/geiger-rs/cargo-geiger) | Detects usage of unsafe Rust in a Rust crate and its dependencies | Source Code | Unsafe code usage | Static Analysis | 2025-08-31 |
| [cargo-vet](https://github.com/mozilla/cargo-vet) | Supply-chain security for Rust - audit your dependencies for trustworthiness | Cargo.lock, Source | Untrusted dependencies | Supply Chain Auditing | 2026-04-19 |
| [cargo-auditable](https://github.com/rust-secure-code/cargo-auditable) | Make production Rust binaries auditable - embed dependency info into binaries | Binary | Dependency vulnerabilities in production binaries | Binary Auditing | 2026-07-24 |
| [cargo-scan](https://github.com/PLSysSec/cargo-scan) | A tool for auditing Rust crates - scans for unsafe patterns and security-sensitive operations. Paper: [Auditing Rust Crates Effectively, ESOP'26](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_15) | Source Code, MIR | Unsafe patterns, Security-sensitive operations | Static Analysis | 2026-07-25 |
| [cargo-udeps](https://github.com/est31/cargo-udeps) | Find unused dependencies in Cargo.toml | Cargo.toml | Unused dependencies | Dependency Analysis | 2026-04-29 |
| [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) | Scan your Rust crate for semver violations | Rust ABI | Semver violations | Static Analysis | 2026-08-20 |
| [cargo-safety](https://github.com/alexkehayias/cargo-safety) | Provides safety checks for Rust projects by finding all uses of unsafe code in dependencies | Source Code | Unsafe code usage | Static Analysis | 2018-01-07 |

---

## Academic Papers

### Static Analysis Papers (no source code yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| Rupair | Rupair: Towards Automatic Buffer Overflow Detection and Rectification for Rust. [Rupair, ACSAC'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, MIR | Buffer Overflow | Data-flow Analysis |
| CRUST | CRUST: Towards a Unified Cross-Language Program Analysis Framework for Rust. [CRUST, QRS'22](https://ieeexplore.ieee.org/document/10062430) | CRustIR based on MIR | Security (CFI vilation, Meta Data Leaking, Format String Attack), Memory issues(Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow) | Program Analysis Framework |
| ACORN | ACORN: Towards a Holistic Cross-Language Program Analysis for Rust. [ACORN](https://csslab-ustc.github.io/publications/2023/acorn.pdf) | Wasm | Security (Tainted Variable, Dangerous Function, Format String Attack), Memory issues (Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow) | Program Analysis Framework |
| Yu Zhang | Static Deadlock Detection for Rust Programs. [Yu Zhang](https://arxiv.org/abs/2401.01114) | MIR | Deadlock | Data-flow Analysis |
| Yu Zhang | Two Birds One Stone: Effective Static Detection of Resource and Communication Deadlocks in Rust Programs. [Automated Software Engineering'26](https://arxiv.org/abs/2401.01114) | MIR | Resource deadlock, Communication deadlock | Data-flow Analysis |
| Zeyang Zhuang, Wei Meng, Michael R. Lyu | Rusted Types: Static Detection of Rust Type Confusion Bugs. [ICSE'26](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/54/Rusted-Types-Static-Detection-of-Rust-Type-Confusion-Bugs) | MIR | Type confusion, Unsafe conversion bugs | Inter-procedural data-flow analysis |
| RustGuard authors | RustGuard: A Compile-Time Verification Framework for Memory Safety in Distributed Rust Applications. [ICPCSN'26](https://ieeexplore.ieee.org/document/11543784/) | MIR | Distributed ownership, Causal lifetime, Resource/communication conflicts | Ownership and causality graphs |
| Kaiwen Zhang | Automatically Transform Rust Source to Petri Nets for Checking Deadlocks. [Kaiwen Zhang](https://arxiv.org/abs/2212.02754) | MIR | Deadlock | Petri Nets |
| RustC4 | Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency. [ASE'24](https://dl.acm.org/doi/10.1145/3691620.3695010) | AST | Code Comment Inconsistency | LLM |
| RustC4++ | RustC4++: Improving Rust Code-Comment Inconsistency Detection via Hybrid LLM and Static Analysis. [OOPSLA'26](https://dl.acm.org/doi/epdf/10.1145/3800689) | AST | Code Comment Inconsistency | LLM, Static Analysis, SMT |
| HALURust | HALURust: Exploiting Hallucinations of Large Language Models to Detect Vulnerabilities in Rust. [arXiv'25](https://arxiv.org/abs/2503.10793) | Source Code | Vulnerabilities | LLM, Static Analysis |
| CULPA | CULPA: Universal Detection of Memory-Safety Bugs in Unsafe Rust Through the Lens of Safety Requirements. [USENIX Security'26](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-hung-mao) | Unsafe Rust, Library APIs | Memory-safety bugs caused by violated safety requirements | Safety-requirement predicates, Requirement Graph, Static Analysis |
| RUXt | Compositional Bug Detection for Internally Unsafe Libraries: A Logical Approach to Type Unsoundness. [ECOOP'25](https://doi.org/10.4230/LIPIcs.ECOOP.2025.5) | Safe APIs with internally unsafe implementations | Type unsoundness, Undefined Behavior | Incorrectness Separation Logic, Under-approximate Compositional Symbolic Execution |
| craft | Automated Fault Tree Generation for Rust Programs. [EDCC'24](https://doi.ieeecomputersociety.org/10.1109/EDCC61798.2024.00022) | - | Fault Tree | Static Program Analysis |
| PanicFI | An Infrastructure for Fixing Panic Bugs in Real-World Rust Programs. [PanicFI](https://www.arxiv.org/pdf/2408.03262) | HIR, AST | Fixing Panic Bugs | Pattern Matching |
| rustc++ | rustc++: Facilitating Advanced Analysis of Rust Code. [rustc++](https://dl.acm.org/doi/epdf/10.1145/3722041.3723102) | MIR, LLVM IR | Enhance MIR & pass metadata for analysis | Metadata |

### Dynamic Analysis Papers (no source code yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| Zhiyong Ren | Detect Stack Overflow Bugs in Rust via Improved Fuzzing Technique. [Zhiyong Ren, SEKE'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, HIR, MIR, LLVM IR | Stack Overflow | Fuzzing |
| Rustcheck | Safety Enhancement of Unsafe Rust via Dynamic Program Analysis. [Rustcheck, QRS-C'23](https://ieeexplore.ieee.org/document/10429951) | MIR | Memory vulnerabilities | Static Program Analysis, Instrumentation |
| RUSTY | A Fuzzing Tool for Rust. [Poster@ACSAC'20](https://www.acsac.org/2020/program/poster-wips/2020-3-RUSTY%20%20A%20Fuzzing%20Tool%20for%20Rust.pdf) | - | Vulnerabilities | Fuzzing, Concolic Testing, Property-based Testing |
| Rust-twins | Automatic Rust Compiler Testing through Program Mutation and Dual Macros Generation. [ASE'24](https://wzyang.cn/files/Rust_twins.pdf) | AST, HIR | Rust compiler crashes and differences | Differential testing, mutation, macroize components, LLM |
| LiteRSan | LiteRSan: Lightweight Memory Safety Via Rust-specific Program Analysis and Selective Instrumentation. [arxiv](https://arxiv.org/pdf/2509.16389) | MIR, LLVM IR | Memory access bugs | Fuzzing |
| FRIES | Fuzzing Rust Library Interactions via Efficient Ecosystem-Guided Target Generation. [FRIES, ISSTA'24](https://dl.acm.org/doi/pdf/10.1145/3650212.3680348) | MIR | Rust API interactions | Fuzzing |
| PanicKiller | Don't Panic! Finding Bugs Hidden Behind Rust Runtime Safety Checks. Zeyang Zhuang, Zilun Wang, Wei Meng, Michael R. Lyu. [CCS'25, pp. 186–200](https://dl.acm.org/doi/10.1145/3719027.3765142) | LLVM IR, Cross-IR | Bugs hidden behind runtime safety checks, Unsafe-code vulnerabilities | Cross-IR analysis, Dynamic taint analysis, Input prioritization/mutation, Fuzzing |

### Verification Papers (no source code yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| GillianRust | A hybrid approach to semi-automated Rust verification. [GillianRust](https://arxiv.org/abs/2403.15122) | Unsafe Code Supported | - | Separation Logic based Hybrid Verification |
| UnsafeCop | Towards Memory Safety for Real-World Unsafe Rust Code with Practical Bounded Model checking. [UnsafeCop, FM'24](https://link.springer.com/chapter/10.1007/978-3-031-71177-0_19) | - | Memory safety issues | Bounded Model Checking |
| SAFE | Automated Proof Generation for Rust Code via Self-Evolution. [SAFE](https://arxiv.org/abs/2410.15756) | Rust Code With Docstring, Verus | - | Verus Verifier, LLM |
| PanicCheck | Broadly Enabling KLEE to Effortlessly Find Unrecoverable Errors. [PanicCheck, ICSE-SEIP'24](https://doi.org/10.1145/3639477.3639714) | LLVM IR | Panic | KLEE |
| Converos | Converos: Practical Model Checking for Verifying Rust OS Kernel Concurrency. [ATC'25](https://www.usenix.org/system/files/atc25-tang.pdf) | PlusCal/TLA+ | Concurrency | Conformance Checking |
| Tas & Jacobs | Towards Verifying Unsafe Rust Programs Against Rust's Pointer-Aliasing Restrictions. [arXiv'26](https://arxiv.org/abs/2603.28326) | Unsafe Rust | Pointer-aliasing violations | Modular Program Logic, Rust Aliasing Semantics |

---

## Thanks

Thanks to the following awesome works:

1. https://github.com/analysis-tools-dev/static-analysis?tab=readme-ov-file#rust
2. https://github.com/analysis-tools-dev/dynamic-analysis?tab=readme-ov-file#rust
3. [A Survey of Rust Language Security Research](https://link.oversea.cnki.net/doi/10.19363/J.cnki.cn10-1380/tn.2023.11.06)
4. [RefinedRust: A Type System for High-Assurance Verification of Rust Programs](https://dl.acm.org/doi/10.1145/3656422)
5. [Verifying the Rust Standard Library](https://www.soundandcomplete.org/vstte2024/vstte2024-invited.pdf)

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
