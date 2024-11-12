# Awesome Rust checkers

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Contributions welcomed!

## Table of contents

- [Awesome Rust checkers](#awesome-rust-checkers)
  - [Table of contents](#table-of-contents)
  - [Linters](#linters)
  - [Static Checkers](#static-checkers)
  - [Dynamic Checkers](#dynamic-checkers)
  - [Verifiers](#verifiers)

## Linters

| Name | Description | Working on | Bug types | Technology | Maintenance |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [clippy](https://github.com/rust-lang/rust-clippy) | A bunch of lints to catch common mistakes and improve your Rust code. | HIR | Versatile | Pattern matching | ★★★★★ |
| [dylint](https://github.com/trailofbits/dylint) | Run Rust lints from dynamic libraries | HIR | Versatile | Pattern matching | ★★★★★ |

## Static Checkers

| Name | Description | Working on | Bug Types | Technology | Maintenance |
| -----| ----------- | ---------- | ----------|-----------| ----------- |
| [MIRAI](https://github.com/facebookexperimental/MIRAI) | Rust mid-level IR Abstract Interpreter | MIR | Panic, Security bugs, Correctness | Abstract Interpretation | ★★★★★ |
| [lockbud](https://github.com/BurtonQin/lockbud) | Statically detect common memory and concurrrency bugs in Rust. Paper: [Safety Issues in Rust, TSE'24](https://songlh.github.io/paper/rust-tse.pdf) | MIR | Double-Lock, Conflicting-Lock-Order, Atomicity-Violation, Use-After-Free, Invalid-Free, Panic Locations | Data-flow Analysis | ★★★★★ |
|[RAP (formerly SafeDrop)](https://github.com/Artisan-Lab/RAP) | Rust Analysis Platform. Paper: [SafeDrop, TOSEM'22](https://dl.acm.org/doi/10.1145/3542948) | MIR | Use-After-Free, Double-Free | Data-flow Analysis | ★★★★★ |
|[RCanary](https://github.com/Artisan-Lab/rCanary) | Detecting Memory Leaks Across Semi-automated Memory Management Boundary in Rust. [RCanary, TSE'24](https://arxiv.org/pdf/2308.04787) | HIR, MIR | Memory Leaks | Static Program Analysis, Model Checking | ★★★☆☆ |
|[Rudra](https://github.com/sslab-gatech/Rudra)| Rust Memory Safety & Undefined Behavior Detection. Paper: [Rudra, SOSP'21](https://dl.acm.org/doi/abs/10.1145/3477132.3483570) | HIR, MIR | Memory safety when panicked, Higher Order Invariant, Send Sync Variance | Data-flow Analysis | ★★★☆☆ |
|[Yuga](https://github.com/vnrst/Yuga) | Automatically Detecting Lifetime Annotation Bugs in the Rust Language. Paper: [Yuga, ICSE'24](https://arxiv.org/abs/2310.08507) | HIR, MIR |  Lifetime Annotation Bugs | Data-flow Analysis | ★★★★☆ |
|[MirChecker](https://github.com/lizhuohua/rust-mir-checker)| A Simple Static Analysis Tool for Rust. Paper: [MirChecker, CCS'21](https://dl.acm.org/doi/10.1145/3460120.3484541) | MIR | Panic (including numerical), Lifetime Corruption (memory issues) | Abstract Interpretation | ★★☆☆☆ |
|[FFIChecker](https://github.com/lizhuohua/rust-ffi-checker) | A Static Analysis Tool For Detecting Memory Management Bugs Between Rust and C/C++. Paper: [FFIChecker, ESORICS'22](https://dl.acm.org/doi/10.1007/978-3-031-17143-7_33) | LLVM IR | Memory issues across the Rust/C FFI | Abstract Interpretation | ★☆☆☆☆ |
|[RUPTA](https://github.com/rustanlys/rupta) | Supports pointer/alias analysis for Rust, operating on Rust MIR. It currently offers callsite-based pointer analysis. Paper: [RUPTA, CC'24](https://dl.acm.org/doi/10.1145/3640537.3641574) | MIR | Not bugs, for callgraph construction| Callsite-based pointer analysis | ★★★★★ |
|[Charon](https://github.com/AeneasVerif/charon) | Interface with the rustc compiler for the purpose of program verification. Paper: [Charon](https://arxiv.org/pdf/2410.18042) | MIR, LLBC | An Analysis Framework for Rust | Convert MIR to LLBC for analysis | ★★★★★ |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| Rupair | Rupair: Towards Automatic Buffer Overflow Detection and Rectification for Rust. [Rupair, ACSAC'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, MIR | Buffer Overflow | Data-flow Analysis |
| CRUST| CRUST: Towards a Unified Cross-Language Program Analysis Framework for Rust. [CRUST, QRS'22](https://ieeexplore.ieee.org/document/10062430) | CRustIR based on MIR | Security (CFI vilation, Meta Data Leaking, Format String Attack), Memory issues(Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow) | Program Analysis Framework |
| ACORN | ACORN: Towards a Holistic Cross-Language Program Analysis for Rust. [ACORN](https://csslab-ustc.github.io/publications/2023/acorn.pdf) | Wasm | Security (Tainted Variable, Dangerous Function, Format String Attack), Memory issues (Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow)  | Program Analysis Framework |
| Yu Zhang | Static Deadlock Detection for Rust Programs. [Yu Zhang](https://arxiv.org/abs/2401.01114) | MIR | Deadlock | Data-flow Analysis |
| Kaiwen Zhang | Automatically Transform Rust Source to Petri Nets for Checking Deadlocks. [Kaiwen Zhang](https://arxiv.org/abs/2212.02754) | MIR | Deadlock | Petri Nets |
| RustC4 | Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency. [ASE'24](https://dl.acm.org/doi/10.1145/3691620.3695010) | AST | Code Comment Inconsistency | LLM |

## Dynamic Checkers

| Name | Description | Working on | Bug Types | Technology | Maintenance |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [miri](https://github.com/rust-lang/miri) | An interpreter for Rust's mid-level intermediate representation | MIR | Undefined Behavior | Abstract Interpretation | ★★★★★ |
| [cargo-careful](https://github.com/RalfJung/cargo-careful) | Execute Rust code carefully, with extra checking along the way | - | Undefined Behavior | Enable Debug Assertion in std | ★★★★★ |
| [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) | Command line helpers for fuzzing | - | - | Fuzzing | ★★★★★ |
| [Loom](https://github.com/tokio-rs/loom)| Concurrency permutation testing tool for Rust. | Source Code | Concurrency Bugs | Permutation testing | ★★★★★ |
| [ERASAN](https://github.com/S2-Lab/ERASan) | Efficient Rust Address Sanitizer. Paper: [IEEES&P'24](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a239/1WPcYZde4BW) | - | Memory Access Bugs | Fuzzing | ★★★★★ |
| [Automated-Fuzzer](https://github.com/qarmin/Automated-Fuzzer) | Simple tool to create broken files and checking them with special apps | - | Panic | Fuzzing | ★★★★★ |
| [RULF](https://github.com/Artisan-Lab/RULF)| Fuzz Target Generator for Rust libraries. Paper: [RULF, ASE'21](https://dl.acm.org/doi/abs/10.1109/ASE51524.2021.9678813) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | ★★★☆☆ |
| [RPG](https://github.com/wcventure/PERIOD)<sup>1</sup>| RPG: Rust Library Fuzzing with Pool-based Fuzz Target. Paper: [RPG, ICSE'24](https://dl.acm.org/doi/10.1145/3597503.3639102) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | ★★☆☆☆ |
| [SyRust](https://kilthub.cmu.edu/articles/code/SyRust_Artifact_PLDI2021_Artifact/14356976) | Automatic Testing of Rust Libraries with Semantic-Aware Program Synthesis. Paper: [SyRust, PLDI'21](https://dl.acm.org/doi/pdf/10.1145/3453483.3454084)| - | - | Program Synthesis | ★☆☆☆☆ |
| [NADER](https://zenodo.org/records/5484436)| Automatic Context-Aware Safety Enhancement for Rust. Paper: [OOPSLA'21](https://dl.acm.org/doi/pdf/10.1145/3485480) | MIR, Source Code | Unchecked Indexing | API Replacing | ★☆☆☆☆ |
| [casr](https://github.com/ispras/casr)<sup>2</sup> | collect crash (or UndefinedBehaviorSanitizer error) reports, triage, and estimate severity. Paper: [Casr-Cluster, ISPRAS'21](https://www.doi.org/10.1109/ISPRAS53967.2021.00012), [Ivannikov Memorial Workshop'24](https://arxiv.org/abs/2405.18174)| Crash Reports from ASan, UBSan, GDB | - | Analyze crashes| ★★★★★ |
| [FRIES](https://github.com/SSCT-Lab/FRIES) | Fuzzing Rust Library Interactions via Efficient Ecosystem-Guided Target Generation. Paper: [FRIES, ISSTA'24](https://dl.acm.org/doi/pdf/10.1145/3650212.3680348) | MIR | Rust API interactions | Fuzzing | ★★★☆☆ |
|[rustsmith](https://github.com/rustsmith/rustsmith) | A randomized program fuzzer for the Rust programming language . Paper: [rustsmith, ISSTA'23](https://rustsmith.github.io/docs/rustsmith-paper.pdf) [rustsmith, thesis](https://rustsmith.github.io/docs/rustsmith-thesis.pdf) | AST | Rust compiler bugs | Differential testing | ★★★☆☆ |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| CrabSandwich | CrabSandwich: Fuzzing Rust with Rust. [CrabSandwich, Fuzzing'23](https://dl.acm.org/doi/abs/10.1145/3605157.3605176)| LLVM IR | Out-of-bounds, Panic | Fuzzing |
| Zhiyong Ren | Detect Stack Overflow Bugs in Rust via Improved Fuzzing Technique. [Zhiyong Ren, SEKE'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, HIR, MIR, LLVM IR | Stack Overflow | Fuzzing |
| Rustcheck | Safety Enhancement of Unsafe Rust via Dynamic Program Analysis. [Rustcheck, QRS-C'23](https://ieeexplore.ieee.org/document/10429951) | MIR | Memory vulnerabilities | Static Program Analysis, Instrumentation |
| RUSTY | A Fuzzing Tool for Rust. [Poster@ACSAC'20](https://www.acsac.org/2020/program/poster-wips/2020-3-RUSTY%20%20A%20Fuzzing%20Tool%20for%20Rust.pdf) | - | Vulnerabilities | Fuzzing, Concolic Testing, Property-based Testing |
| Rust-twins | Automatic Rust Compiler Testing through Program Mutation and Dual Macros Generation. [ASE'24](hhttps://wzyang.cn/files/Rust_twins.pdf) | AST, HIR | Rust compiler crashes and differences  |  Differential testing, mutation, macroize components, LLM |


1. The link may be incorrect. See [here](https://wcventure.github.io/EnPage/opensource/2023-12-05-RPG).
2. casr analyze the results of dynamic checkers instead of performing dynamic analysis itself. Thanks [zjp-CN](https://github.com/zjp-CN) for recommending casr.

## Verifiers

| Name | Description | Working on | Bug Types | Technology | Maintenance |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [kani](https://github.com/model-checking/kani/) | The Kani Rust Verifier is a bit-precise model checker for Rust. Paper: [kani, ICSE-SEIP'22](https://dl.acm.org/doi/abs/10.1145/3510457.3513031)| MIR | Memory safety, User-specified assertions, Panics, Unexpected behavior (e.g., arithmetic overflows)  | Model Checking | ★★★★★ |
| [prusti](https://github.com/viperproject/prusti-dev) | A static verifier for Rust, based on the Viper verification infrastructure. Paper: [prusti, NFM'22 ](https://link.springer.com/chapter/10.1007/978-3-031-06773-0_5) | Viper | Panic (inluding arithmetic), User-specified assertions | Symbolic Execution  | ★★★★☆ |
| [crux-mir](https://github.com/GaloisInc/crucible/tree/master/crux-mir) | A static simulator for Rust programs | - | - | Symbolic Testing | ★★★★☆ |
| [verus](https://github.com/verus-lang/verus) | Verified Rust for low-level systems code. Paper: [verus, OOPSLA'23](https://dl.acm.org/doi/pdf/10.1145/3586037), [SOSP'24](https://www.microsoft.com/en-us/research/publication/verus-a-practical-foundation-for-systems-verification/) | - | - | SMT-based Verification<sup>5</sup> | ★★★★★ |
| [flux](https://github.com/flux-rs/flux) | flux is a refinement type checker for Rust. Paper: [flux, PLDI'23](https://dl.acm.org/doi/10.1145/3591283)| - | - | - | ★★★★★ |
| [Aeneas](https://github.com/AeneasVerif/aeneas) | A verification toolchain for Rust programs. Paper: [Aeneas, ICFP'22](https://dl.acm.org/doi/abs/10.1145/3547647) | LLBC (for safe Rust only) | - | - | ★★★★★ |
| [RustBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/) | Formal (and machine-checked) safety proof for a language representing a realistic subset of Rust. Paper: [RustBelt, POPL'18](https://dl.acm.org/doi/10.1145/3158154) | 𝜆Rust| - | - | ★★★★★ |
| [RustHorn](https://github.com/hopv/rust-horn) | A CHC-based automated verifier for Rust [RustHorn, TOPLAS'21](https://dl.acm.org/doi/full/10.1145/3462205) | MIR | - | - | ★★★★☆ |
| [Creusot](https://github.com/creusot-rs/creusot) | A deductive verifier for Rust code. [Creusot, ICFEM'22](https://inria.hal.science/hal-03737878/file/main.pdf) | WhyML | Panics, overflows, Assertion failures | Deductive Verification | ★★★★★ |
| [RustHornBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/-/tree/masters/rusthornbelt) | A Semantic Foundation for Functional Verification of Rust Programs with Unsafe Code. Paper: [RustHornBelt, PLDI'22](https://dl.acm.org/doi/10.1145/3519939.3523704)| 𝜆Rust | - | - | ★★☆☆☆ |
| [RefinedRust<sup>1</sup>](https://gitlab.mpi-sws.org/lgaeher/refinedrust-dev) | A Type System for High-Assurance Verification of Rust Programs. Paper: [RefinedRust, PLDI'24](https://dl.acm.org/doi/10.1145/3656422)| Radium | - | - | ★★★★★ |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| GillianRust | A hybrid approach to semi-automated Rust verification. [GillianRust](https://arxiv.org/abs/2403.15122)| Unsafe Code Supported | - | Separation Logic based Hybrid Verification<sup>5</sup> |
| UnsafeCop | Towards Memory Safety for Real-World Unsafe Rust Code with Practical Bounded Model checking. [UnsafeCop, FM'24](https://link.springer.com/chapter/10.1007/978-3-031-71177-0_19)| - | Memory safety issues | Bounded Model Checking |
| SAFE | Automated Proof Generation for Rust Code via Self-Evolution. [SAFE](https://arxiv.org/abs/2410.15756) | Rust Code With Docstring, Verus | - | Verus Verifier, LLM |

1. Thanks to [jedbrown](https://users.rust-lang.org/u/jedbrown) for recommending RefinedRust and other Rust-related verification tools.

Thanks to the following awesome works:

1. https://github.com/analysis-tools-dev/static-analysis?tab=readme-ov-file#rust
2.  https://github.com/analysis-tools-dev/dynamic-analysis?tab=readme-ov-file#rust
3. [A Survey of Rust Language Security Research](https://link.oversea.cnki.net/doi/10.19363/J.cnki.cn10-1380/tn.2023.11.06)
4. [RefinedRust: A Type System for High-Assurance Verification of Rust Programs](https://dl.acm.org/doi/10.1145/3656422)
5. [Verifying the Rust Standard Library](https://www.soundandcomplete.org/vstte2024/vstte2024-invited.pdf)




