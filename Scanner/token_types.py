from enum import Enum


class TokenType(Enum):
    AddOp = 1 # +
    SubtractOp = 2 # -
    MultiplyOp = 3 # *
    DivideOp = 4 # /
    EqualToOp = 5 # =
    NotEqualToOp = 6 # <>
    GreaterThanOp = 7 # >
    LessThanOp = 8 # <
    GreaterThanOrEqualOp = 9 # >=
    LessThanOrEqualOp = 10 # <=
    OpenSquareBracket = 11 # [
    CloseSquareBracket = 12 # ]
    Dot = 13 # .
    Comma = 14 # ,
    AssignmentOp = 15 # :=
    Colon = 16 # :
    SemiColon = 17 # ;
    OpenParenthesis = 18 # (
    CloseParenthesis = 19 # )
    BitwiseNot = 20 # ~
    BitwiseAnd = 21 # &
    BitwiseOrVerticalBar = 22 # |
    BitwiseOrExclamationMark = 23 # !
    AndKeyword = 24
    FileKeyword = 25
    ModKeyword = 26
    RepeatKeyword = 27
    ArrayKeyword = 28
    ForKeyword = 29
    NilKeyword = 30
    SetKeyword = 31
    BeginKeyword = 32
    ForwardKeyword = 33
    NotKeyword = 34
    ThenKeyword = 35
    CaseKeyword = 36
    FunctionKeyword = 37
    OfKeyword = 38
    ToKeyword = 39
    ConstKeyword = 40
    GotoKeyword = 41
    OrKeyword = 42
    TypeKeyword = 43
    DivKeyword = 44
    IfKeyword = 45
    PackedKeyword = 46
    UntilKeyword = 47
    DoKeyword = 48
    InKeyword = 49
    ProcedureKeyword = 50
    VarKeyword = 51
    DowntoKeyword = 52
    LabelKeyword = 53
    ProgramKeyword = 54
    WhileKeyword = 55
    ElseKeyword = 56
    MainKeyword = 57
    RecordKeyword = 58
    WithKeyword = 59
    DefineKeyword = 60
    ExternKeyword = 61
    ExternalKeyword = 62
    ModuleKeyword = 63
    OtherwiseKeyword = 64
    PrivateKeyword = 65
    PublicKeyword = 66
    StaticKeyword = 67
    UnivKeyword = 68
    BooleanKeyword = 69
    CharKeyword = 70
    FalseKeyword = 71
    IntegerKeyword = 72
    ReadKeyword = 73
    ReadlnKeyword = 74
    RealKeyword = 75
    TrueKeyword = 76
    WriteKeyword = 77
    WritelnKeyword = 78
    StringKeyword = 79
    DoubleQuotations = 80 # "
    SingleQuotations = 81 # '
    Identifier = 82
    IntegerConstant = 83
    RealConstant = 84
    EndKeyword = 85
    OpenBraces = 86 # {
    CloseBraces = 87 # }
    StringConstant = 88
    UsesKeyword = 89
    Error = 90
    EOF = 91


token_types_map = {token.value: token.name for token in TokenType}

